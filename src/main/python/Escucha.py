from antlr4 import ErrorNode, TerminalNode
from  compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from Squeleton import TablaSimbolos
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
        # aca deberia chequear que cuando se declare una variable ya no este en la tabla de simbolos
        # if ctx.children is not None and len(ctx.children) > 1:
        #     nombre_variable = ctx.getChild(1).getText()  # Suponiendo que el nombre está en el índice 1
        #     tipo_dato = ctx.getChild(0).getText()  # Suponiendo que el tipo está en el índice 0
            
        #     print("Número de hijos: " + str(len(ctx.children)))
        #     print("Nombre variable: " + nombre_variable)
        variable = TablaSimbolos.Variable(ctx.getChild(1).getText(), ctx.getChild(0).getText())
        self.tabla.add_contexto(variable)
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
        funcion = TablaSimbolos.Funcion(ctx.getChild().getText(), ctx)
        self.tabla.add_contexto(funcion)
        self.tabla.add_contexto(ctx)
        print("\tTokens: " + ctx.getText())
        
    def exitInic(self, ctx):#cambiar inic a true
        return super().exitInic(ctx)
    def exitAsignacion(self, ctx):#cambiar usado a true
        return super().exitAsignacion(ctx)
        
    def visitTerminal(self, node: TerminalNode):
        # print(" ---> Token: " + node.getText())
        self.numTokens += 1
        
    def visitErrorNode(self, node: ErrorNode):
        print(" ---> ERROR SINTACTICO")
        print(node.getText())
        
    def enterEveryRule(self, ctx):
        self.numNodos += 1