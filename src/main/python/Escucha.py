from antlr4 import ErrorNode, TerminalNode
from  compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from Squeleton import *
import re
# mientras se va creando el arbol, avanza
# para analisis semantico

# TODO no se estan agregando las cosas al contexto actual (p.e.: declaracion)
# TODO hacer que las otras funciones que tienen bloque se imprima el contexto como en WHILE
# TODO todavia no anda usar una funcion en expresion aritmetica
# TODO imprimir numeros de linea

class Escucha (compiladoresListener) :
    numTokens = 0 #tokens son las hojas
    numNodos = 0
    tabla = TablaSimbolos.get_instancia()
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("\t\tComienza la compilacion")
        #print(self.tabla.__str__())

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("\t\tFin de la compilacion")
        # print("Se encontraron")
        # print("\tNodos: " + str(self.numNodos))
        # print("\tTokens: " + str(self.numTokens))
        print(self.tabla.__str__())
        self.tabla.mostrarVarsSinUsar()
        self.tabla.del_Contexto()
        
    
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        print("\t\tEnter WHILE")
        
    def exitIwhile(self, ctx: compiladoresParser.IwhileContext):
        print(self.tabla.add_contexto("WHILE").__str__())
        print("\t\tFIN WHILE")
        
        # print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        # print("\tTokens: " + ctx.getText())
        
        self.tabla.del_Contexto()
        
    def enterDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        print("\t\t Declaracion")
        
    def exitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        # se solucionadoria con if anidado y llamando al buscar por separado en cada caso
        nombreVariable = ctx.getChild(1).getText()
        tipoDeDato = ctx.getChild(0).getText()

        variable = ID(nombreVariable, tipoDeDato)
        
        #Las busquedas si devuelven None es porque encontraron algo
        busquedaGlobal = self.tabla.buscar_global(nombreVariable)
        busquedaLocal = self.tabla.buscar_local(nombreVariable)
        
        if busquedaLocal is None:
            if busquedaGlobal is None:
            #print('"'+nombreVariable+'"'+" no fue declarada previamente")
                self.tabla.add_identificador(variable)
                print("\033[1;32m" +"Nombre variable: " + nombreVariable+ " es declarada en el contexto actual"+"\033[0m")
            else:
                self.tabla.add_identificador(variable)
                print("\033[1;33m" +"Advertencia: La variable: " + nombreVariable+ "es redeclarada en el contexto actual"+"\033[0m")
        else:
            print("\033[1;31m" + f"ERROR SEMANTICO: La variable '{nombreVariable}' fue declarada previamente en el contexto local."+ "\033[0m")
            return
        
        
    def enterIfor(self, ctx: compiladoresParser.IforContext):
        print("\t\tEnter FOR")
        
    def exitIfor(self, ctx: compiladoresParser.IforContext):
        self.tabla.add_contexto("FOR")
        print("\t\tFIN FOR")
        # print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        # print("\tTokens: " + ctx.getText())
        self.tabla.del_Contexto()
        
    def enterIif(self, ctx: compiladoresParser.IifContext):
        print("\t\tENTER IF")
    
    def exitIif(self, ctx: compiladoresParser.IifContext):
        self.tabla.add_contexto("IF")
        print(ctx.IF.getText())
        print("\t\tEXIT IF")
        # print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        # print("\tTokens: " + ctx.getText())
        self.tabla.del_Contexto()
        
    def enterElse(self, ctx: compiladoresParser.ElseContext):
        print("\t\tENTER ELSE")
    
    def exitElse(self, ctx: compiladoresParser.ElseContext):
        self.tabla.add_contexto("ELSE")
        print("\t\tEXIT del ELSE")
        # print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        # print("\tTokens: " + ctx.getText())
        self.tabla.del_Contexto()
        
    def enterProtofun(self, ctx: compiladoresParser.ProtofunContext):
        print("\t\tFUNCION")
        
    def exitProtofun(self, ctx: compiladoresParser.ProtofunContext):
        #Se agregan () para diferenciar de las variables y por si una funcion y una variable se llaman igual
        nombreFuncion= ctx.getChild(1).getText()
        funcion = ID(nombreFuncion, ctx.getChild(0).getText())
        busquedaLocal = self.tabla.buscar_local(nombreFuncion)
        busquedaGlobal = self.tabla.buscar_global(nombreFuncion)
        if busquedaLocal is None and busquedaGlobal is None:
            print("\033[1;32m" +f"Se inicializó la variable '{nombreFuncion}' en el contexto actual."+ "\033[0m")
            funcion.set_inicializado()  # Marcar como inicializada
            self.tabla.add_identificador(funcion)
        elif busquedaLocal is not None:
            print("\033[1;31m" +"ERROR SEMANTICO: La variable '" + nombreFuncion + "' ya está declarada"+ "\033[0m")
        elif busquedaGlobal is not None:
            print("\033[1;31m" + "ERROR SEMANTICO: La variable '" + nombreFuncion + "' ya está declarada"+ "\033[0m")
        print("\t" + ctx.getText()) 
        
    def exitInic(self, ctx):
        nombreVariable = ctx.getChild(1).getText()
        # Si el nombre de la variable contiene un '=', extraemos solo el nombre
        if '=' in nombreVariable:
            nombreVariable = nombreVariable.split('=')[0].strip()

        # Chequear si existe en el contexto actual o global
        busquedaLocal = self.tabla.buscar_local(nombreVariable)
        busquedaGlobal = self.tabla.buscar_global(nombreVariable)
        tipoDeDato = ctx.getChild(0).getText()
        variable = ID(nombreVariable, tipoDeDato)

        # Si la variable no existe en ningún contexto, la inicializamos y agregamos
        if busquedaLocal is None and busquedaGlobal is None:
            print("\033[1;32m" +f"Se inicializó la variable '{nombreVariable}' en el contexto actual."+ "\033[0m")
            variable.set_inicializado()  # Marcar como inicializada
            self.tabla.add_identificador(variable)
        elif busquedaLocal is not None:
            print("\033[1;31m" +"ERROR SEMANTICO: La variable '" + nombreVariable + "' ya está declarada en el contexto local."+ "\033[0m")
        elif busquedaGlobal is not None:
            print("\033[1;31m" + "ERROR SEMANTICO: La variable '" + nombreVariable + "' ya está declarada en el contexto global."+ "\033[0m")

    def exitAsignacion(self, ctx):
        operacion = ctx.getChild(0).getText()
        # Verificar si el nombre de la variable de la izquierda contiene un '='
        if '=' in operacion:
            nombreVariableIzquierda = operacion.split('=')[0].strip()
            expresionDerecha = operacion.split('=')[1].strip()
            
            busquedaLocalIzquierda = self.tabla.buscar_local(nombreVariableIzquierda)
            busquedaGlobalIzquierda = self.tabla.buscar_global(nombreVariableIzquierda)

            # Asegurarse de que la variable izquierda está declarada
            if busquedaLocalIzquierda is None and busquedaGlobalIzquierda is None:
                print("\033[1;31m" + f"ERROR SEMANTICO: La variable '{nombreVariableIzquierda}' no fue declarada previamente."+ "\033[0m")
                return
            
            # Obtener el tipo de la variable izquierda
            tipoIzquierda = (busquedaLocalIzquierda.tipoDato if busquedaLocalIzquierda else busquedaGlobalIzquierda.tipoDato)

            # Procesar la expresión de la derecha, ignorando operadores aritméticos
            terminos = re.split(r'(\+|-|\*|/)', expresionDerecha)
            
            for termino in terminos:
                termino = termino.strip()
                if termino in {'+', '-', '*', '/'}:
                    # Ignorar operadores aritméticos
                    continue
                elif termino.isdigit():
                    # Si es un número, continuar
                    continue
                elif termino.isidentifier():  # Verificar si es un identificador (variable)
                    # Buscar la variable en el contexto
                    busquedaLocalDerecha = self.tabla.buscar_local(termino)
                    busquedaGlobalDerecha = self.tabla.buscar_global(termino)

                    # Verificar que la variable esté declarada
                    if busquedaLocalDerecha is None and busquedaGlobalDerecha is None:
                        print("\033[1;31m" + f"ERROR SEMANTICO: La variable '{termino}' no fue declarada previamente!"+ "\033[0m")
                        return

                    # Obtener el tipo de la variable derecha
                    tipoDerecha = (busquedaLocalDerecha.tipoDato if busquedaLocalDerecha else busquedaGlobalDerecha.tipoDato)

                    # Verificar compatibilidad de tipos
                    if tipoIzquierda != tipoDerecha:
                        print("\033[1;33m" + f"Advertencia: No se puede asignar un valor de tipo '{tipoDerecha}' a una variable de tipo '{tipoIzquierda}'."+ "\033[0m")
                        return
                    
                    # Marcar la variable como usada
                    if busquedaLocalDerecha:
                        busquedaLocalDerecha.set_usado()
                    else:
                        busquedaGlobalDerecha.set_usado()
                else:
                    # Error si no es un número ni una variable válida
                    print("\033[1;31m" + f"ERROR SEMANTICO: El término '{termino}' no es válido en la expresión de asignación."+ "\033[0m")
                    return

            # Si todos los términos son válidos, proceder con la asignación
            print("\033[1;32m" + f"Asignación válida: '{nombreVariableIzquierda}' = '{expresionDerecha}'."+ "\033[0m")
            
            # Marcar la variable izquierda como usada
            if busquedaLocalIzquierda is not None:
                busquedaLocalIzquierda.set_usado()
            else:
                busquedaGlobalIzquierda.set_usado()


    def visitTerminal(self, node: TerminalNode):
        # print(" ---> Token: " + node.getText())
        self.numTokens += 1
        
    def visitErrorNode(self, node: ErrorNode):
        print("\033[1;31m" +" ERROR SINTACTICO"+ "\033[0m")
        print(node.getText())
        
    def enterEveryRule(self, ctx):
        self.numNodos += 1
        