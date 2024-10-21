# Generated from c:/Users/Usuario/OneDrive/Documentos/Facultad/iua/tercero/DHS/dhsprueba/src/main/python/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class compiladoresListener(ParseTreeListener):

    # Enter a parse tree produced by compiladoresParser#si.
    def enterSi(self, ctx:compiladoresParser.SiContext):
        pass

    # Exit a parse tree produced by compiladoresParser#si.
    def exitSi(self, ctx:compiladoresParser.SiContext):
        pass


    # Enter a parse tree produced by compiladoresParser#s.
    def enterS(self, ctx:compiladoresParser.SContext):
        pass

    # Exit a parse tree produced by compiladoresParser#s.
    def exitS(self, ctx:compiladoresParser.SContext):
        pass


    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instrucciones.
    def enterInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instrucciones.
    def exitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instruccion.
    def enterInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instruccion.
    def exitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignacionInt.
    def enterAsignacionInt(self, ctx:compiladoresParser.AsignacionIntContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacionInt.
    def exitAsignacionInt(self, ctx:compiladoresParser.AsignacionIntContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#inst.
    def enterInst(self, ctx:compiladoresParser.InstContext):
        pass

    # Exit a parse tree produced by compiladoresParser#inst.
    def exitInst(self, ctx:compiladoresParser.InstContext):
        pass


    # Enter a parse tree produced by compiladoresParser#opal.
    def enterOpal(self, ctx:compiladoresParser.OpalContext):
        pass

    # Exit a parse tree produced by compiladoresParser#opal.
    def exitOpal(self, ctx:compiladoresParser.OpalContext):
        pass


    # Enter a parse tree produced by compiladoresParser#exp.
    def enterExp(self, ctx:compiladoresParser.ExpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#exp.
    def exitExp(self, ctx:compiladoresParser.ExpContext):
        pass


    # Enter a parse tree produced by compiladoresParser#expPrima.
    def enterExpPrima(self, ctx:compiladoresParser.ExpPrimaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#expPrima.
    def exitExpPrima(self, ctx:compiladoresParser.ExpPrimaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#term.
    def enterTerm(self, ctx:compiladoresParser.TermContext):
        pass

    # Exit a parse tree produced by compiladoresParser#term.
    def exitTerm(self, ctx:compiladoresParser.TermContext):
        pass


    # Enter a parse tree produced by compiladoresParser#t.
    def enterT(self, ctx:compiladoresParser.TContext):
        pass

    # Exit a parse tree produced by compiladoresParser#t.
    def exitT(self, ctx:compiladoresParser.TContext):
        pass


    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#iwhile.
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        pass

    # Exit a parse tree produced by compiladoresParser#iwhile.
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladoresParser#comps.
    def enterComps(self, ctx:compiladoresParser.CompsContext):
        pass

    # Exit a parse tree produced by compiladoresParser#comps.
    def exitComps(self, ctx:compiladoresParser.CompsContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bools.
    def enterBools(self, ctx:compiladoresParser.BoolsContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bools.
    def exitBools(self, ctx:compiladoresParser.BoolsContext):
        pass


    # Enter a parse tree produced by compiladoresParser#factorBool.
    def enterFactorBool(self, ctx:compiladoresParser.FactorBoolContext):
        pass

    # Exit a parse tree produced by compiladoresParser#factorBool.
    def exitFactorBool(self, ctx:compiladoresParser.FactorBoolContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignacionBool.
    def enterAsignacionBool(self, ctx:compiladoresParser.AsignacionBoolContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacionBool.
    def exitAsignacionBool(self, ctx:compiladoresParser.AsignacionBoolContext):
        pass


    # Enter a parse tree produced by compiladoresParser#opbool.
    def enterOpbool(self, ctx:compiladoresParser.OpboolContext):
        pass

    # Exit a parse tree produced by compiladoresParser#opbool.
    def exitOpbool(self, ctx:compiladoresParser.OpboolContext):
        pass


    # Enter a parse tree produced by compiladoresParser#opcomp.
    def enterOpcomp(self, ctx:compiladoresParser.OpcompContext):
        pass

    # Exit a parse tree produced by compiladoresParser#opcomp.
    def exitOpcomp(self, ctx:compiladoresParser.OpcompContext):
        pass


    # Enter a parse tree produced by compiladoresParser#ifor.
    def enterIfor(self, ctx:compiladoresParser.IforContext):
        pass

    # Exit a parse tree produced by compiladoresParser#ifor.
    def exitIfor(self, ctx:compiladoresParser.IforContext):
        pass


    # Enter a parse tree produced by compiladoresParser#init.
    def enterInit(self, ctx:compiladoresParser.InitContext):
        pass

    # Exit a parse tree produced by compiladoresParser#init.
    def exitInit(self, ctx:compiladoresParser.InitContext):
        pass


    # Enter a parse tree produced by compiladoresParser#cond.
    def enterCond(self, ctx:compiladoresParser.CondContext):
        pass

    # Exit a parse tree produced by compiladoresParser#cond.
    def exitCond(self, ctx:compiladoresParser.CondContext):
        pass


    # Enter a parse tree produced by compiladoresParser#iter.
    def enterIter(self, ctx:compiladoresParser.IterContext):
        pass

    # Exit a parse tree produced by compiladoresParser#iter.
    def exitIter(self, ctx:compiladoresParser.IterContext):
        pass


    # Enter a parse tree produced by compiladoresParser#iif.
    def enterIif(self, ctx:compiladoresParser.IifContext):
        pass

    # Exit a parse tree produced by compiladoresParser#iif.
    def exitIif(self, ctx:compiladoresParser.IifContext):
        pass



del compiladoresParser