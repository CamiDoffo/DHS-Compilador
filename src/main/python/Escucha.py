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
        variable = ID(nombreVariable, tipoDeDato)
        
        #Las busquedas si devuelven None es porque encontraron algo
        busquedaGlobal = self.tabla.buscar_global(nombreVariable)
        busquedaLocal = self.tabla.buscar_local(nombreVariable)
        # chequeo que paso (no hace falta) TODO borrar
        if busquedaGlobal is None and busquedaLocal is None :
            print('"'+nombreVariable+'"'+" no fue declarada previamente")
            self.tabla.add_identificador(variable)
        
        print("Nombre variable: " + ctx.getChild(1).getText())
        
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
        funcion = ID(ctx.getChild(1).getText(), ctx.getChild(0).getText())
        self.tabla.add_identificador(funcion)
        print("\tTokens: " + ctx.getText())        
    
    def exitAsignacion(self, ctx: compiladoresParser.AsignacionContext):#cambiar usado a true
        nombreVariable= ctx.getChild(0).getText()
        busquedaLocal = self.tabla.buscar_local(nombreVariable)
        busquedaGlobal = self.tabla.buscar_global(nombreVariable)
        #buscamos si la variable fue declarada globalmente
        if busquedaLocal is not None or busquedaGlobal is not None :
            print("Se inicializo/modifico TU VIEJA SABE DONDE la variable '" + nombreVariable +"'")
            if busquedaGlobal.inicializado is True:
                busquedaGlobal.set_usado()
            else:
                busquedaGlobal.set_inicializado()
            
        
    def visitTerminal(self, node: TerminalNode):
        # print(" ---> Token: " + node.getText())
        self.numTokens += 1
        
    def visitErrorNode(self, node: ErrorNode):
        print(" ---> ERROR SINTACTICO")
        print(node.getText())
        
    def enterEveryRule(self, ctx):
        self.numNodos += 1