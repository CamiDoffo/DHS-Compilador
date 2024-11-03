from antlr4 import ErrorNode, TerminalNode
from  compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from Squeleton import *
# mientras se va creando el arbol, avanza
# para analisis semantico

# TODO ver donde cambiaria usado a true


class Escucha (compiladoresListener) :
    numTokens = 0 #tokens son las hojas
    numNodos = 0
    tabla = TablaSimbolos.get_instancia()
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Comienza la compilacion")

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Fin de la compilacion")
        print("Se encontraron")
        print("\tNodos: " + str(self.numNodos))
        print("\tTokens: " + str(self.numTokens))
        print(self.tabla.__str__())
        self.tabla.del_Contexto()
    
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        print("Enter WHILE")
        
    def exitIwhile(self, ctx: compiladoresParser.IwhileContext):
        self.tabla.add_contexto(ctx)
        print("FIN del WHILE")
        print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
        self.tabla.del_Contexto()
        
    def enterDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        print(" ### Declaracion")
        
    def exitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        #TODO detalle porque imprime que no lo encuentra en los dos contextos
        # se solucionadoria con if anidado y llamando al buscar por separado en cada caso
        nombreVariable = ctx.getChild(1).getText()
        tipoDeDato = ctx.getChild(0).getText()
                # Si el nombre de la variable contiene un '=', tomamos solo la parte anterior
        if '=' in nombreVariable:
            nombreVariable = nombreVariable.split('=')[0].strip()  # Tomamos solo el nombre sin espacios

        variable = ID(nombreVariable, tipoDeDato)
        
        #Las busquedas si devuelven None es porque encontraron algo
        busquedaGlobal = self.tabla.buscar_global(nombreVariable)
        busquedaLocal = self.tabla.buscar_local(nombreVariable)
        # chequeo que paso (no hace falta) TODO borrar
        if busquedaGlobal is None and busquedaLocal is None :
            print('"'+nombreVariable+'"'+" no fue declarada previamente")
            self.tabla.add_identificador(variable)
        
        print("Nombre variable: " + nombreVariable)
        
    def enterIfor(self, ctx: compiladoresParser.IforContext):
        print("Enter FOR")
        
    def exitIfor(self, ctx: compiladoresParser.IforContext):
        self.tabla.add_contexto(ctx)
        print("FIN del FOR")
        print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
        self.tabla.del_Contexto()
        
    def enterIif(self, ctx: compiladoresParser.IifContext):
        print("ENTER IF")
    
    def exitIif(self, ctx: compiladoresParser.IifContext):
        self.tabla.add_contexto(ctx)
        print("EXIT del IF")
        print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
        self.tabla.del_Contexto()
        
    def enterElse(self, ctx: compiladoresParser.ElseContext):
        print("ENTER ELSE")
    
    def exitElse(self, ctx: compiladoresParser.ElseContext):
        self.tabla.add_contexto(ctx)
        print("EXIT del ELSE")
        print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
        self.tabla.del_Contexto()
        
    def enterFunciones(self, ctx: compiladoresParser.FuncionesContext):
        print("FUNCION")
        
    def exitFunciones(self, ctx: compiladoresParser.FuncionesContext):
        #Se agregan () para diferenciar de las variables y por si una funcion y una variable se llaman igual
        funcion = ID(ctx.getChild(1).getText()+"()", ctx.getChild(0).getText())
        self.tabla.add_identificador(funcion)
        print("\tTokens: " + ctx.getText())        
        
        
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
            print("Se inicializó TU VIEJA SABE DONDE la variable '" + nombreVariable + "'")
            print(f"Se inicializó la variable '{nombreVariable}' en el contexto actual.")
            variable.set_inicializado()  # Marcar como inicializada
            self.tabla.add_identificador(variable)
        elif busquedaLocal is not None:
            print("---- ERROR SEMANTICO -----")
            print("El identificador "+nombre+" ya existe en el contexto local!")
            print("La variable '" + nombreVariable + "' ya está declarada en el contexto local.")
        elif busquedaGlobal is not None:
            print("---- ERROR SEMANTICO -----")
            print("El identificador "+nombre+" ya existe en el contexto global!")
            print("La variable '" + nombreVariable + "' ya está declarada en el contexto global.")


    def exitAsignacion(self, ctx):
        nombreVariable = ctx.getChild(0).getText()
        # Si el nombre de la variable contiene un '=', extraemos solo el nombre
        if '=' in nombreVariable:
            nombreVariable = nombreVariable.split('=')[0].strip()

        busquedaLocal = self.tabla.buscar_local(nombreVariable)
        busquedaGlobal = self.tabla.buscar_global(nombreVariable)

        # Si la variable está en el contexto local
        if busquedaLocal is not None:
            print(f"Se intenta modificar la variable '{nombreVariable}' en el contexto local.")
            if busquedaLocal.inicializado:
                print("Se modificó TU VIEJA SABE DONDE la variable '" + nombreVariable + "'")
                busquedaLocal.set_usado()
            else:
                print(f"Error: La variable '{nombreVariable}' debe inicializarse antes de asignarse.")
        # Si la variable está en el contexto global
        elif busquedaGlobal is not None:
            print(f"Se intenta modificar la variable '{nombreVariable}' en el contexto global.")
            if busquedaGlobal.inicializado:
                print("Se modificó TU VIEJA SABE DONDE la variable '" + nombreVariable + "'")
                busquedaGlobal.set_usado()
            else:
                print(f"Error: La variable '{nombreVariable}' debe inicializarse antes de asignarse.")
        else:
            print(f"Error: La variable '{nombreVariable}' no fue declarada previamente.")

    def visitTerminal(self, node: TerminalNode):
        # print(" ---> Token: " + node.getText())
        self.numTokens += 1
        
    def visitErrorNode(self, node: ErrorNode):
        print(" ---> ERROR SINTACTICO")
        print(node.getText())
        
    def enterEveryRule(self, ctx):
        self.numNodos += 1