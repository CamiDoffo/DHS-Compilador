# Generated from compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#programa.
    def visitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instruccion.
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracionGlobal.
    def visitDeclaracionGlobal(self, ctx:compiladoresParser.DeclaracionGlobalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#restoDeclaracion.
    def visitRestoDeclaracion(self, ctx:compiladoresParser.RestoDeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#decItem.
    def visitDecItem(self, ctx:compiladoresParser.DecItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#funcionVoid.
    def visitFuncionVoid(self, ctx:compiladoresParser.FuncionVoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#tipoDatos.
    def visitTipoDatos(self, ctx:compiladoresParser.TipoDatosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#argumento.
    def visitArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#argumentos.
    def visitArgumentos(self, ctx:compiladoresParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instruccionOBloque.
    def visitInstruccionOBloque(self, ctx:compiladoresParser.InstruccionOBloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#iwhile.
    def visitIwhile(self, ctx:compiladoresParser.IwhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#iif.
    def visitIif(self, ctx:compiladoresParser.IifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#ifor.
    def visitIfor(self, ctx:compiladoresParser.IforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacion.
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacionPYC.
    def visitAsignacionPYC(self, ctx:compiladoresParser.AsignacionPYCContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#returnfun.
    def visitReturnfun(self, ctx:compiladoresParser.ReturnfunContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#ids.
    def visitIds(self, ctx:compiladoresParser.IdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#funcionVar.
    def visitFuncionVar(self, ctx:compiladoresParser.FuncionVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#llamadafun.
    def visitLlamadafun(self, ctx:compiladoresParser.LlamadafunContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#exp.
    def visitExp(self, ctx:compiladoresParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#factor.
    def visitFactor(self, ctx:compiladoresParser.FactorContext):
        return self.visitChildren(ctx)



del compiladoresParser