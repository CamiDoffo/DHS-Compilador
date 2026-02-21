from antlr4 import ErrorNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from Squeleton import *
import re

# Constantes de color ANSI
C_VERDE = "\033[1;32m"
C_AMARILLO = "\033[1;33m"
C_ROJO = "\033[1;31m"
C_CIAN = "\033[1;36m"
C_RESET = "\033[0m"

class Escucha(compiladoresListener):
    def __init__(self):
        self.tabla = TablaSimbolos.get_instancia()
        self.error = False

    # =========================================================================
    #  INICIO Y FIN DEL PROGRAMA
    # =========================================================================
    def enterPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print(f"{C_CIAN}Comienza la compilacion{C_RESET}")
        print(f"{C_CIAN}----> CREANDO CONTEXTO GLOBAL{C_RESET}")
        self.tabla.add_contexto("Global")

    def exitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print(f"\n{C_CIAN}\t\tFin de la compilacion{C_RESET}\n")
        # mostrarVarsSinUsar() ya imprime su propio título
        self.tabla.mostrarVarsSinUsar()
        self.tabla.del_Contexto()

    # =========================================================================
    #  DECLARACIONES GLOBALES Y VARIABLES
    # =========================================================================
    def exitDeclaracionGlobal(self, ctx: compiladoresParser.DeclaracionGlobalContext):
        tipo = ctx.getChild(0).getText()
        nombre_principal = ctx.getChild(1).getText()
        ctx_resto = ctx.restoDeclaracion()
        primer_token = ctx_resto.start.text 
        
        if primer_token == '(':
            self.procesarFuncion(nombre_principal, tipo, ctx_resto)
        else:
            self.guardarVariable(tipo, nombre_principal, inicializado=ctx_resto.exp() is not None)
            if ctx_resto.exp():
                self.auditarAsignacion(nombre_principal, ctx_resto.exp(), ctx.start.line)

    def exitDecItem(self, ctx: compiladoresParser.DecItemContext):
        if ctx.parentCtx and isinstance(ctx.parentCtx, compiladoresParser.RestoDeclaracionContext):
            tipo = ctx.parentCtx.parentCtx.getChild(0).getText()
            nombre = ctx.ID().getText()
            inicializado = ctx.exp() is not None
            self.guardarVariable(tipo, nombre, inicializado)
            if inicializado:
                self.auditarAsignacion(nombre, ctx.exp(), ctx.start.line)
                
        elif ctx.parentCtx and isinstance(ctx.parentCtx, compiladoresParser.IforContext):
            tipo_ctx = ctx.parentCtx.tipoDatos()
            tipo = tipo_ctx.getText() if tipo_ctx else "int"
            nombre = ctx.ID().getText()
            self.guardarVariable(tipo, nombre, inicializado=True)
            if ctx.exp():
                self.auditarAsignacion(nombre, ctx.exp(), ctx.start.line)

    def exitFuncionVoid(self, ctx: compiladoresParser.FuncionVoidContext):
        nombre = ctx.getChild(1).getText()
        self.procesarFuncion(nombre, "void", ctx)

    # =========================================================================
    #  MANEJO DE CONTEXTOS Y BLOQUES (ENTER/EXIT)
    # =========================================================================
    def enterBloque(self, ctx: compiladoresParser.BloqueContext):
        padre = ctx.parentCtx
        
        if isinstance(padre, compiladoresParser.RestoDeclaracionContext):
            abuelo = padre.parentCtx
            tipo = abuelo.getChild(0).getText()
            nombre = abuelo.getChild(1).getText()
            if '(' in nombre: nombre = nombre.split('(')[0]
            print(f"{C_CIAN}DEBUG: Función Detectada (Con Tipo) -> {tipo} {nombre}{C_RESET}")
            self.tabla.add_contexto("FUNCION")
            self.inyectarArgumentos(padre)
            
        elif isinstance(padre, compiladoresParser.FuncionVoidContext):
            nombre = padre.getChild(1).getText()
            print(f"{C_CIAN}DEBUG: Función Detectada (Void) -> void {nombre}{C_RESET}")
            self.tabla.add_contexto("FUNCION")
            self.inyectarArgumentos(padre)
        else:
            self.tabla.add_contexto("BLOQUE")

    def exitBloque(self, ctx: compiladoresParser.BloqueContext):
        self.tabla.del_Contexto()

    # Estructuras de control (IF, WHILE, FOR)
    def enterIif(self, ctx: compiladoresParser.IifContext):
        print(f"{C_CIAN}\t\tENTER IF{C_RESET}")
    def exitIif(self, ctx: compiladoresParser.IifContext):
        print(f"{C_CIAN}\t\tEXIT IF{C_RESET}")

    def enterIwhile(self, ctx: compiladoresParser.IwhileContext):
        print(f"{C_CIAN}\t\tENTER WHILE{C_RESET}")
    def exitIwhile(self, ctx: compiladoresParser.IwhileContext):
        print(f"{C_CIAN}\t\tEXIT WHILE{C_RESET}")

    def enterIfor(self, ctx: compiladoresParser.IforContext):
        print(f"{C_CIAN}\t\tENTER FOR{C_RESET}")
    def exitIfor(self, ctx: compiladoresParser.IforContext):
        print(f"{C_CIAN}\t\tEXIT FOR{C_RESET}")

    # =========================================================================
    #  ASIGNACIONES Y LLAMADAS
    # =========================================================================
    def exitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        nombre_var = ctx.ID().getText()
        linea = ctx.start.line 
        self.auditarAsignacion(nombre_var, ctx.exp(), linea)

    def auditarAsignacion(self, nombre_var, ctx_exp, linea):
        var = self.tabla.buscar_local(nombre_var) or self.tabla.buscar_global(nombre_var)
        if var is None:
            print(f"{C_ROJO}Línea {linea}: ERROR SEMANTICO: Variable '{nombre_var}' no declarada.{C_RESET}")
            self.error = True
            return
            
        var.set_inicializado()
        exp_texto = ctx_exp.getText()
        
        # Auditar uso de variables en el lado derecho (la expresión)
        self.auditarExpresion(ctx_exp, linea)
        
        # Verificación de tipos básica
        if var.tipoDato in ['float', 'double'] and exp_texto.isdigit():
            print(f"{C_AMARILLO}Línea {linea}: Advertencia: No se puede asignar un valor de tipo 'int' a una variable de tipo '{var.tipoDato}'.{C_RESET}")
            
        print(f"{C_VERDE}Línea {linea}: Asignación válida: '{nombre_var}' = '{exp_texto}'.{C_RESET}")

    def exitFuncionVar(self, ctx: compiladoresParser.FuncionVarContext):
        nombreFuncion = ctx.ID().getText()
        linea = ctx.start.line
        busquedaGlobal = self.tabla.buscar_global(nombreFuncion)

        if busquedaGlobal is None:
            print(f"{C_ROJO}Línea {linea}: ERROR SEMANTICO: La función '{nombreFuncion}' no declarada.{C_RESET}")
            self.error = True
            return

        args_pasados = ctx.ids().getText().split(',') if ctx.ids() and ctx.ids().getText() else []
        args_pasados = [a for a in args_pasados if a]
        
        definicion_args = getattr(busquedaGlobal, 'args', [])
        if len(args_pasados) != len(definicion_args):
            print(f"{C_ROJO}Línea {linea}: ERROR SEMANTICO: '{nombreFuncion}' espera {len(definicion_args)} argumentos, recibio {len(args_pasados)}.{C_RESET}")
            self.error = True

    # =========================================================================
    #  MÉTODOS AUXILIARES
    # =========================================================================
    def guardarVariable(self, tipo, nombre, inicializado=False):
        var = Variable(nombre, tipo)
        if inicializado: var.set_inicializado()
        
        if self.tabla.buscar_local(nombre) is None:
            self.tabla.add_identificador(var)
        else:
            print(f"{C_ROJO}Línea 0: ERROR SEMANTICO: Variable '{nombre}' ya declarada localmente.{C_RESET}")
            self.error = True

    def procesarFuncion(self, nombre, tipo, ctx_args):
        if '(' in nombre: nombre = nombre.split('(')[0]

        funcion = Funcion(nombre, tipo)
        funcion.args = []

        argumentos_ctx = ctx_args.argumentos()
        if argumentos_ctx is not None:
            for arg_ctx in argumentos_ctx.argumento():
                tipo_arg = arg_ctx.tipoDatos().getText()
                funcion.args.append(tipo_arg)
        
        funcion.set_inicializado()
        if self.tabla.buscar_local(nombre) is None:
            self.tabla.add_identificador(funcion)

    def inyectarArgumentos(self, ctx_args):
        argumentos_ctx = ctx_args.argumentos()
        if argumentos_ctx is not None:
            for arg_ctx in argumentos_ctx.argumento():
                tipo_arg = arg_ctx.tipoDatos().getText()
                nombre_arg = arg_ctx.ID().getText()
                var = Variable(nombre_arg, tipo_arg)
                var.set_inicializado() 
                self.tabla.add_identificador(var)

    def auditarExpresion(self, ctx_exp, linea):
        tokens = re.findall(r'[a-zA-Z_]\w*', ctx_exp.getText())
        palabras_reservadas = {'TRUE', 'FALSE'}
        
        for token in tokens:
            if token in palabras_reservadas: continue
            var = self.tabla.buscar_local(token) or self.tabla.buscar_global(token)
            if var:
                var.set_usado()
                if not var.inicializado and not hasattr(var, 'args'):
                    print(f"{C_AMARILLO}Línea {linea}: ADVERTENCIA: Variable '{token}' usada sin inicializar.{C_RESET}")
            else:
                print(f"{C_ROJO}Línea {linea}: ERROR SEMANTICO: Variable '{token}' no declarada.{C_RESET}")
                self.error = True

    def visitErrorNode(self, node: ErrorNode):
        print(f"{C_ROJO}ERROR SINTACTICO: {node.getText()}{C_RESET}")
        self.error = True