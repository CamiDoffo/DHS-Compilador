from antlr4 import ErrorNode, TerminalNode
from  compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
# mientras se va creando el arbol, avanza

class Escucha (compiladoresListener) :
    numTokens = 0 #tokens son las hojas
    numNodos = 0
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Comienza la compilacion")

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Fin de la compilacion")
        print("Se encontraron")
        print("\tNodos: " + str(self.numNodos))
        print("\tTokens: " + str(self.numTokens))
        
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        print("Enter WHILE")
        print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
        
    def exitIwhile(self, ctx: compiladoresParser.IwhileContext):
        print("FIN del WHILE")
        print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
        
    def enterDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        print(" ### Declaracion")
        
    def exitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        print("Nombre variable: " + ctx.getChild(1).getText())
        
    def visitTerminal(self, node: TerminalNode):
        # print(" ---> Token: " + node.getText())
        self.numTokens += 1
        
    def visitErrorNode(self, node: ErrorNode):
        print(" ---> ERROR")
        print(node.getText())
        
    def enterEveryRule(self, ctx):
        self.numNodos += 1
        
    def enterIfor(self, ctx):
        print("Enter FOR")
        print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
    def exitIfor(self, ctx):
        print("FIN del FOR")
        print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())