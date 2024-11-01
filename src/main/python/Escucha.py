from antlr4 import ErrorNode, TerminalNode
from  compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from Squeleton import TablaSimbolos
import urllib.request
# mientras se va creando el arbol, avanza
# para analisis semantico
urllib.request.urlopen("https://youtu.be/EwGTAU6ypiw?si=tnTMPNHtsZVyeKx5")
class Escucha (compiladoresListener) :
    numTokens = 0 #tokens son las hojas
    numNodos = 0
    tabla = TablaSimbolos()
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Comienza la compilacion")
        self.tabla.add_contexto(ctx)

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Fin de la compilacion")
        print("Se encontraron")
        print("\tNodos: " + str(self.numNodos))
        print("\tTokens: " + str(self.numTokens))
        self.tabla.del_Contexto()
    
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        print("Enter WHILE")
        print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
        self.tabla.add_contexto(ctx)
        
    def exitIwhile(self, ctx: compiladoresParser.IwhileContext):
        print("FIN del WHILE")
        print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
        self.tabla.del_Contexto(ctx)
        
    def enterDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        print(" ### Declaracion")
        # aca deberia chequear que cuando se declare una variable ya no este en la tabla de simbolos
        self.tabla.add_contexto(ctx)
        
        
    def exitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        print("Nombre variable: " + ctx.getChild(1).getText())
        self.tabla.del_Contexto()
        
    def enterIfor(self, ctx):
        print("Enter FOR")
        print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
        self.tabla.add_contexto(ctx)
        
    def exitIfor(self, ctx):
        print("FIN del FOR")
        print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
        self.tabla.del_Contexto()
        
    def enterIif(self, ctx):
        print("ENTER IF")
        print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
        self.tabla.add_contexto(ctx)
    
    def exitIif(self, ctx):
        print("EXIT del IF")
        print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
        self.tabla.del_Contexto()
        
    def enterElse(self, ctx):
        print("ENTER ELSE")
        print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
        self.tabla.add_contexto(ctx)
    
    def exitElse(self, ctx):
        print("EXIT del ELSE")
        print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " + ctx.getText())
        self.tabla.del_Contexto()
        
    def visitTerminal(self, node: TerminalNode):
        # print(" ---> Token: " + node.getText())
        self.numTokens += 1
        
    def visitErrorNode(self, node: ErrorNode):
        print(" ---> ERROR")
        print(node.getText())
        
    def enterEveryRule(self, ctx):
        self.numNodos += 1