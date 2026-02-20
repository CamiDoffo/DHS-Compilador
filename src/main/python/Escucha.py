from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from Squeleton import *
import re

class Escucha(compiladoresListener):
    numTokens = 0
    numNodos = 0
    tabla = TablaSimbolos.get_instancia()
    error = False

    def __init__(self):
        # Archivo de log
        self.log_file = open('./output/Compilacion.txt', 'w', encoding='utf-8')
        self.nivel_indentacion = 0

    def write_log(self, mensaje, indentar=True):
        if indentar:
            self.log_file.write('\t' * self.nivel_indentacion + mensaje + '\n')
        else:
            self.log_file.write(mensaje + '\n')
        self.log_file.flush()

    def __del__(self):
        if hasattr(self, 'log_file'):
            self.log_file.close()

    # =========================================================================
    #  INICIO Y FIN DEL PROGRAMA (Contexto Global)
    # =========================================================================
    def enterPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("\t\tComienza la compilacion")
        print("----> CREANDO CONTEXTO GLOBAL")
        self.tabla.add_contexto("Global")

    def exitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("\t\tFin de la compilacion")
        # print(self.tabla.__str__()) # Descomentar para ver la tabla completa al final
        self.tabla.mostrarVarsSinUsar()
        self.tabla.del_Contexto()

    # =========================================================================
    #  DECLARACIÓN DE VARIABLES (Locales y Globales)
    # =========================================================================

    # --- Variables Globales (Regla declaracionGlobal) ---
    def exitDeclaracionGlobal(self, ctx: compiladoresParser.DeclaracionGlobalContext):
        # Verificamos si es una VARIABLE mirando el resto (si no empieza con '(' )
        ctx_resto = ctx.getChild(2)
        primer_token = ctx_resto.start.text 
        ultimo_token = ctx_resto.stop.text # Miramos cómo termina

        # SI EMPIEZA CON '(' Y TERMINA CON ';' ES UN PROTOTIPO
        if primer_token == '(' and ultimo_token == ';':
            tipo = ctx.getChild(0).getText()
            nombre = ctx.getChild(1).getText()
            print(f"DEBUG: Prototipo Detectado -> {tipo} {nombre}")
            # Llamamos a procesarFuncion pero le avisamos que es prototipo (puedes adaptar la función)
            self.procesarFuncion(nombre, tipo, ctx_resto, es_prototipo=True)

        elif primer_token != '(':
            tipo = ctx.getChild(0).getText()
            nombre_primero = ctx.getChild(1).getText()
            
            self.guardarVariable(tipo, nombre_primero)
            
            # Guardamos las demás si existen (ej: int a, b, c;)
            texto_resto = ctx_resto.getText()
            if ',' in texto_resto and '=' not in texto_resto:
                vars_extra = texto_resto.replace(';', '').split(',')
                for v in vars_extra:
                    v = v.strip()
                    if v and v != ',':
                        self.guardarVariable(tipo, v)

    # --- Variables Locales (Regla declaracion) ---
    def exitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        tipoDeDato = ctx.getChild(0).getText()
        linea = ctx.start.line
        
        for token_id in ctx.ID(): 
            nombreVariable = token_id.getText()
            variable = Variable(nombreVariable, tipoDeDato)
            
            busquedaLocal = self.tabla.buscar_local(nombreVariable)
            busquedaGlobal = self.tabla.buscar_global(nombreVariable)
            
            if busquedaLocal is None:
                self.tabla.add_identificador(variable)
                if busquedaGlobal is None:
                    print(f"\033[1;32mLínea {linea}: La variable '{nombreVariable}' se declaró en el contexto actual.\033[0m")
                else:
                    print(f"\033[1;33mLínea {linea}: Advertencia: La variable '{nombreVariable}' oculta una variable global.\033[0m")
            else:
                print(f"\033[1;31mLínea {linea}: ERROR SEMÁNTICO: La variable '{nombreVariable}' ya fue declarada localmente.\033[0m")
                self.error = True

    # --- Inicialización con Asignación (int a = 10;) ---
    def exitInic(self, ctx):
        nombreVariable = ctx.getChild(1).getText()
        linea = ctx.start.line
        
        if '=' in nombreVariable:
            nombreVariable = nombreVariable.split('=')[0].strip()

        busquedaLocal = self.tabla.buscar_local(nombreVariable)
        tipoDeDato = ctx.getChild(0).getText()
        variable = Variable(nombreVariable, tipoDeDato)

        if busquedaLocal is None:
            print(f"\033[1;32mLínea {linea}: La variable '{nombreVariable}' se inicializó correctamente.\033[0m")
            variable.set_inicializado()
            self.tabla.add_identificador(variable)
        else:
            print(f"\033[1;31mLínea {linea}: ERROR SEMANTICO: Variable '{nombreVariable}' redeclarada.\033[0m")
            self.error = True

    # =========================================================================
    #  DEFINICIÓN DE FUNCIONES (Manejo de Contextos)
    # =========================================================================

    def enterBloque(self, ctx: compiladoresParser.BloqueContext):
        padre = ctx.parentCtx
        
        # CASO A: Función con Tipo (int suma() { ... })
        if isinstance(padre, compiladoresParser.RestoDeclaracionContext):
            if padre.start.text == '(':
                abuelo = padre.parentCtx
                tipo = abuelo.getChild(0).getText()
                nombre = abuelo.getChild(1).getText()
                print(f"DEBUG: Función Detectada (Con Tipo) -> {tipo} {nombre}")
                self.procesarFuncion(nombre, tipo, padre)

        # CASO B: Función Void (void main() { ... })
        elif isinstance(padre, compiladoresParser.FuncionVoidContext):
            tipo = "void"
            nombre = padre.getChild(1).getText()
            print(f"DEBUG: Función Detectada (Void) -> {tipo} {nombre}")
            self.procesarFuncion(nombre, tipo, padre)
        
        # CASO C: Bloque suelto (if, while, for, o simplemente { })
        else:
            # ESTRICTO ESTILO C: Creamos un nuevo contexto temporal
            self.write_log("ENTER BLOQUE (Scope Local)", indentar=True)
            self.tabla.add_contexto("BLOQUE")

    def exitBloque(self, ctx: compiladoresParser.BloqueContext):
        padre = ctx.parentCtx
        es_funcion_tipo = isinstance(padre, compiladoresParser.RestoDeclaracionContext) and padre.start.text == '('
        es_funcion_void = isinstance(padre, compiladoresParser.FuncionVoidContext)
        
        # Si salimos de una función, cerramos el contexto de la función
        if es_funcion_tipo or es_funcion_void:
            self.cerrarContextoFuncion()
            
        # Si salimos de un bloque normal (if, while), cerramos su propio contexto
        else:
            self.write_log("EXIT BLOQUE (Destruyendo Scope Local)", indentar=True)
            self.tabla.del_Contexto()

    def exitFuncionVoid(self, ctx):
        self.cerrarContextoFuncion()

    # =========================================================================
    #  ASIGNACIONES Y LLAMADAS A FUNCIONES (Validación Semántica)
    # =========================================================================

    def exitAsignacion(self, ctx):
        operacion = ctx.getChild(0).getText()
        linea = ctx.start.line  
        
        if '=' in operacion:
            nombreVariableIzquierda = operacion.split('=')[0].strip()
            expresionDerecha = operacion.split('=')[1].strip()
            
            # Buscar variable izquierda
            varIzquierda = self.tabla.buscar_local(nombreVariableIzquierda) or self.tabla.buscar_global(nombreVariableIzquierda)

            if varIzquierda is None:
                print(f"\033[1;31mLínea {linea}: ERROR SEMANTICO: Variable '{nombreVariableIzquierda}' no declarada.\033[0m")
                self.error = True
                return
            
            tipoIzquierda = varIzquierda.tipoDato

            # Validación básica de la derecha
            terminos = re.split(r'(\+|-|\*|/)', expresionDerecha)
            
            for termino in terminos:
                termino = termino.strip()
                if termino in {'+', '-', '*', '/'} or re.match(r'^\d+(\.\d+)?$', termino):
                    continue
                
                # Si es Variable o Función
                if termino.isidentifier() or (re.search(r'[()]', termino)):
                    if '(' in termino: termino = re.sub(r'\(.*?\)', '', termino) 
                    
                    varDerecha = self.tabla.buscar_local(termino) or self.tabla.buscar_global(termino)

                    if varDerecha is None:
                        print(f"\033[1;31mLínea {linea}: ERROR SEMANTICO: Variable '{termino}' no declarada.\033[0m")
                        self.error = True
                        return
                    
                    varDerecha.set_usado()
                    
                    # Advertencia de inicialización
                    if not varDerecha.inicializado:
                         print(f"\033[1;33mLínea {linea}: ADVERTENCIA: Variable '{termino}' usada sin inicializar.\033[0m")

                    # Validación de tipos
                    if tipoIzquierda != varDerecha.tipoDato:
                        print(f"\033[1;33mLínea {linea}: Advertencia: No se puede asignar un valor de tipo '{varDerecha.tipoDato}' a una variable de tipo '{tipoIzquierda}'.\033[0m")
                        return

            # Si todo sale bien, marcamos la izquierda como inicializada
            varIzquierda.set_inicializado()
            print(f"\033[1;32mLínea {linea}: Asignación válida: '{nombreVariableIzquierda}' = '{expresionDerecha}'.\033[0m")   

    def exitFuncionVar(self, ctx):
        nombreFuncion = ctx.getChild(0).getText().split('(')[0].strip()
        args = ctx.getChild(2).getText().split(',')
        args = [arg for arg in args if arg.strip()] # Filtro vacíos

        linea = ctx.start.line
        busquedaGlobal = self.tabla.buscar_global(nombreFuncion)

        # 1. Existe función?
        if busquedaGlobal is None:
            print(f"\033[1;31mLínea {linea}: ERROR SEMANTICO: La función '{nombreFuncion}' no fue declarada.\033[0m")
            self.error = True
            return

        # 2. Cantidad argumentos
        definicion_args = getattr(busquedaGlobal, 'args', [])
        if len(args) != len(definicion_args):
            print(f"\033[1;31mLínea {linea}: ERROR SEMANTICO: Cantidad argumentos incorrecta. Esperados {len(definicion_args)}, recibidos {len(args)}.\033[0m")
            self.error = True
            return

        # 3. Tipos argumentos
        for i, nombreArgCall in enumerate(args):
            varCall = self.tabla.buscar_local(nombreArgCall) or self.tabla.buscar_global(nombreArgCall)
            
            if varCall is None:
                if not (nombreArgCall.isdigit() or '.' in nombreArgCall):
                      print(f"\033[1;31mLínea {linea}: ERROR SEMANTICO: Argumento '{nombreArgCall}' no declarado.\033[0m")
                continue
            
            tipoEsperado = definicion_args[i]
            tipoRecibido = varCall.tipoDato
            
            if tipoEsperado != tipoRecibido:
                print(f"\033[1;31mLínea {linea}: ERROR SEMANTICO: Tipo incorrecto en arg {i+1}. Esperado '{tipoEsperado}', recibido '{tipoRecibido}'.\033[0m")

    # =========================================================================
    #  ESTRUCTURAS DE CONTROL (Prints de seguimiento)
    # =========================================================================
    def enterIwhile(self, ctx): print("\t\tENTER WHILE")
    def exitIwhile(self, ctx):  print("\t\tEXIT WHILE")
    def enterIfor(self, ctx):   print("\t\tENTER FOR")
    def exitIfor(self, ctx):    print("\t\tEXIT FOR")
    def enterIif(self, ctx):    print("\t\tENTER IF")
    def exitIif(self, ctx):     print("\t\tEXIT IF")

    # =========================================================================
    #  MÉTODOS AUXILIARES Y HERRAMIENTAS
    # =========================================================================
    def procesarFuncion(self, nombre, tipo, ctx_donde_estan_args, es_prototipo=False):
        if '(' in nombre: nombre = nombre.split('(')[0]

        funcion = Funcion(nombre, tipo)
        funcion.args = []

        texto = ctx_donde_estan_args.getText()
        if '(' in texto and ')' in texto:
            contenido = texto.split('(')[1].split(')')[0]
            if contenido.strip():
                tokens = contenido.split(',')
                for t in tokens:
                    if 'int' in t: funcion.args.append('int')
                    elif 'float' in t: funcion.args.append('float')
                    elif 'bool' in t: funcion.args.append('bool')
                    elif 'double' in t: funcion.args.append('double')
        
        funcion.set_inicializado()
        # LÓGICA DE PROTOTIPOS
        busqueda = self.tabla.buscar_local(nombre)
        
        if busqueda is None:
            # No existía, la agregamos (puede ser el prototipo o la función directa)
            self.tabla.add_identificador(funcion)
        else:
            # Ya existía. Si estamos entrando al BLOQUE (no es prototipo),
            # asumimos que lo que estaba en la tabla era el prototipo. Es válido.
            if es_prototipo:
                print(f"\033[1;33mAdvertencia: Prototipo '{nombre}' re-declarado.\033[0m")
        
        # Solo abrimos contexto (scope) si NO es un prototipo
        if not es_prototipo:
            self.write_log(f"ENTER FUNCION {nombre}", indentar=True)
            self.tabla.add_contexto("FUNCION")

    def guardarVariable(self, tipo, nombre):
        var = Variable(nombre, tipo)
        var.set_inicializado(False)
        self.tabla.add_identificador(var)
        self.write_log(f"Declarada variable global: {tipo} {nombre}")

    def cerrarContextoFuncion(self):
        self.write_log("EXIT FUNCION", indentar=True)
        if len(self.tabla.contextos) > 2:
            self.tabla.del_Contexto()

    def visitTerminal(self, node: TerminalNode):
        self.numTokens += 1
        
    def visitErrorNode(self, node: ErrorNode):
        print(f"\033[1;31m ERROR SINTACTICO: {node.getText()} \033[0m")
        self.error = True
        
    def enterEveryRule(self, ctx):
        self.numNodos += 1