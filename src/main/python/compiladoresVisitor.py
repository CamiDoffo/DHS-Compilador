# Generated from c:/Users/Usuario/OneDrive/Documentos/Facultad/iua/tercero/DHS/compilador/src/main/python/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#si.
    def visitSi(self, ctx:compiladoresParser.SiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#s.
    def visitS(self, ctx:compiladoresParser.SContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#programa.
    def visitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instruccion.
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracion.
    def visitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacionInt.
    def visitAsignacionInt(self, ctx:compiladoresParser.AsignacionIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacion.
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#inst.
    def visitInst(self, ctx:compiladoresParser.InstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#opal.
    def visitOpal(self, ctx:compiladoresParser.OpalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#exp.
    def visitExp(self, ctx:compiladoresParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#expPrima.
    def visitExpPrima(self, ctx:compiladoresParser.ExpPrimaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#term.
    def visitTerm(self, ctx:compiladoresParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#t.
    def visitT(self, ctx:compiladoresParser.TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#factor.
    def visitFactor(self, ctx:compiladoresParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#iwhile.
    def visitIwhile(self, ctx:compiladoresParser.IwhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#comps.
    def visitComps(self, ctx:compiladoresParser.CompsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bools.
    def visitBools(self, ctx:compiladoresParser.BoolsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#factorBool.
    def visitFactorBool(self, ctx:compiladoresParser.FactorBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacionBool.
    def visitAsignacionBool(self, ctx:compiladoresParser.AsignacionBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#opbool.
    def visitOpbool(self, ctx:compiladoresParser.OpboolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#opcomp.
    def visitOpcomp(self, ctx:compiladoresParser.OpcompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#ifor.
    def visitIfor(self, ctx:compiladoresParser.IforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#init.
    def visitInit(self, ctx:compiladoresParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#cond.
    def visitCond(self, ctx:compiladoresParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#iter.
    def visitIter(self, ctx:compiladoresParser.IterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#iif.
    def visitIif(self, ctx:compiladoresParser.IifContext):
        return self.visitChildren(ctx)



del compiladoresParser