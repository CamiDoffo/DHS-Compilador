# Generated from compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class compiladoresListener(ParseTreeListener):

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


    # Enter a parse tree produced by compiladoresParser#declaracionGlobal.
    def enterDeclaracionGlobal(self, ctx:compiladoresParser.DeclaracionGlobalContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracionGlobal.
    def exitDeclaracionGlobal(self, ctx:compiladoresParser.DeclaracionGlobalContext):
        pass


    # Enter a parse tree produced by compiladoresParser#restoDeclaracion.
    def enterRestoDeclaracion(self, ctx:compiladoresParser.RestoDeclaracionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#restoDeclaracion.
    def exitRestoDeclaracion(self, ctx:compiladoresParser.RestoDeclaracionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#decItem.
    def enterDecItem(self, ctx:compiladoresParser.DecItemContext):
        pass

    # Exit a parse tree produced by compiladoresParser#decItem.
    def exitDecItem(self, ctx:compiladoresParser.DecItemContext):
        pass


    # Enter a parse tree produced by compiladoresParser#funcionVoid.
    def enterFuncionVoid(self, ctx:compiladoresParser.FuncionVoidContext):
        pass

    # Exit a parse tree produced by compiladoresParser#funcionVoid.
    def exitFuncionVoid(self, ctx:compiladoresParser.FuncionVoidContext):
        pass


    # Enter a parse tree produced by compiladoresParser#tipoDatos.
    def enterTipoDatos(self, ctx:compiladoresParser.TipoDatosContext):
        pass

    # Exit a parse tree produced by compiladoresParser#tipoDatos.
    def exitTipoDatos(self, ctx:compiladoresParser.TipoDatosContext):
        pass


    # Enter a parse tree produced by compiladoresParser#argumento.
    def enterArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#argumento.
    def exitArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#argumentos.
    def enterArgumentos(self, ctx:compiladoresParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by compiladoresParser#argumentos.
    def exitArgumentos(self, ctx:compiladoresParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instruccionOBloque.
    def enterInstruccionOBloque(self, ctx:compiladoresParser.InstruccionOBloqueContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instruccionOBloque.
    def exitInstruccionOBloque(self, ctx:compiladoresParser.InstruccionOBloqueContext):
        pass


    # Enter a parse tree produced by compiladoresParser#iwhile.
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        pass

    # Exit a parse tree produced by compiladoresParser#iwhile.
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        pass


    # Enter a parse tree produced by compiladoresParser#iif.
    def enterIif(self, ctx:compiladoresParser.IifContext):
        pass

    # Exit a parse tree produced by compiladoresParser#iif.
    def exitIif(self, ctx:compiladoresParser.IifContext):
        pass


    # Enter a parse tree produced by compiladoresParser#ifor.
    def enterIfor(self, ctx:compiladoresParser.IforContext):
        pass

    # Exit a parse tree produced by compiladoresParser#ifor.
    def exitIfor(self, ctx:compiladoresParser.IforContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignacionPYC.
    def enterAsignacionPYC(self, ctx:compiladoresParser.AsignacionPYCContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacionPYC.
    def exitAsignacionPYC(self, ctx:compiladoresParser.AsignacionPYCContext):
        pass


    # Enter a parse tree produced by compiladoresParser#returnfun.
    def enterReturnfun(self, ctx:compiladoresParser.ReturnfunContext):
        pass

    # Exit a parse tree produced by compiladoresParser#returnfun.
    def exitReturnfun(self, ctx:compiladoresParser.ReturnfunContext):
        pass


    # Enter a parse tree produced by compiladoresParser#ids.
    def enterIds(self, ctx:compiladoresParser.IdsContext):
        pass

    # Exit a parse tree produced by compiladoresParser#ids.
    def exitIds(self, ctx:compiladoresParser.IdsContext):
        pass


    # Enter a parse tree produced by compiladoresParser#funcionVar.
    def enterFuncionVar(self, ctx:compiladoresParser.FuncionVarContext):
        pass

    # Exit a parse tree produced by compiladoresParser#funcionVar.
    def exitFuncionVar(self, ctx:compiladoresParser.FuncionVarContext):
        pass


    # Enter a parse tree produced by compiladoresParser#llamadafun.
    def enterLlamadafun(self, ctx:compiladoresParser.LlamadafunContext):
        pass

    # Exit a parse tree produced by compiladoresParser#llamadafun.
    def exitLlamadafun(self, ctx:compiladoresParser.LlamadafunContext):
        pass


    # Enter a parse tree produced by compiladoresParser#exp.
    def enterExp(self, ctx:compiladoresParser.ExpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#exp.
    def exitExp(self, ctx:compiladoresParser.ExpContext):
        pass


    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        pass



del compiladoresParser