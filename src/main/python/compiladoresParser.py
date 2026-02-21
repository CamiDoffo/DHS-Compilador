# Generated from src/main/antlr4/compiladores.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,225,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,1,0,1,1,5,1,51,8,1,10,1,12,1,54,
        9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,67,8,2,1,3,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,78,8,4,1,4,1,4,3,4,82,8,4,1,4,
        1,4,5,4,86,8,4,10,4,12,4,89,9,4,1,4,3,4,92,8,4,1,5,1,5,1,5,3,5,97,
        8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,106,8,6,1,7,1,7,1,8,1,8,1,8,
        1,9,1,9,1,9,5,9,116,8,9,10,9,12,9,119,9,9,3,9,121,8,9,1,10,1,10,
        1,10,1,10,1,11,1,11,3,11,129,8,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,144,8,13,1,14,1,14,1,14,
        3,14,149,8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,
        1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,3,17,170,8,17,1,18,
        1,18,1,18,5,18,175,8,18,10,18,12,18,178,9,18,3,18,180,8,18,1,19,
        1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,5,21,
        208,8,21,10,21,12,21,211,9,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,3,22,223,8,22,1,22,0,1,42,23,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,0,4,1,0,1,4,1,0,24,26,
        1,0,22,23,2,0,21,21,27,29,235,0,46,1,0,0,0,2,52,1,0,0,0,4,66,1,0,
        0,0,6,68,1,0,0,0,8,91,1,0,0,0,10,93,1,0,0,0,12,98,1,0,0,0,14,107,
        1,0,0,0,16,109,1,0,0,0,18,120,1,0,0,0,20,122,1,0,0,0,22,128,1,0,
        0,0,24,130,1,0,0,0,26,136,1,0,0,0,28,145,1,0,0,0,30,159,1,0,0,0,
        32,163,1,0,0,0,34,169,1,0,0,0,36,179,1,0,0,0,38,181,1,0,0,0,40,186,
        1,0,0,0,42,189,1,0,0,0,44,222,1,0,0,0,46,47,3,2,1,0,47,48,5,0,0,
        1,48,1,1,0,0,0,49,51,3,4,2,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,1,
        0,0,0,52,53,1,0,0,0,53,3,1,0,0,0,54,52,1,0,0,0,55,67,3,6,3,0,56,
        67,3,12,6,0,57,67,3,24,12,0,58,67,3,28,14,0,59,67,3,26,13,0,60,67,
        3,32,16,0,61,62,3,34,17,0,62,63,5,15,0,0,63,67,1,0,0,0,64,67,3,40,
        20,0,65,67,3,20,10,0,66,55,1,0,0,0,66,56,1,0,0,0,66,57,1,0,0,0,66,
        58,1,0,0,0,66,59,1,0,0,0,66,60,1,0,0,0,66,61,1,0,0,0,66,64,1,0,0,
        0,66,65,1,0,0,0,67,5,1,0,0,0,68,69,3,14,7,0,69,70,5,33,0,0,70,71,
        3,8,4,0,71,7,1,0,0,0,72,73,5,13,0,0,73,74,3,18,9,0,74,77,5,14,0,
        0,75,78,3,20,10,0,76,78,5,15,0,0,77,75,1,0,0,0,77,76,1,0,0,0,78,
        92,1,0,0,0,79,80,5,20,0,0,80,82,3,42,21,0,81,79,1,0,0,0,81,82,1,
        0,0,0,82,87,1,0,0,0,83,84,5,18,0,0,84,86,3,10,5,0,85,83,1,0,0,0,
        86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,90,1,0,0,0,89,87,1,
        0,0,0,90,92,5,15,0,0,91,72,1,0,0,0,91,81,1,0,0,0,92,9,1,0,0,0,93,
        96,5,33,0,0,94,95,5,20,0,0,95,97,3,42,21,0,96,94,1,0,0,0,96,97,1,
        0,0,0,97,11,1,0,0,0,98,99,5,5,0,0,99,100,5,33,0,0,100,101,5,13,0,
        0,101,102,3,18,9,0,102,105,5,14,0,0,103,106,3,20,10,0,104,106,5,
        15,0,0,105,103,1,0,0,0,105,104,1,0,0,0,106,13,1,0,0,0,107,108,7,
        0,0,0,108,15,1,0,0,0,109,110,3,14,7,0,110,111,5,33,0,0,111,17,1,
        0,0,0,112,117,3,16,8,0,113,114,5,18,0,0,114,116,3,16,8,0,115,113,
        1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,121,
        1,0,0,0,119,117,1,0,0,0,120,112,1,0,0,0,120,121,1,0,0,0,121,19,1,
        0,0,0,122,123,5,16,0,0,123,124,3,2,1,0,124,125,5,17,0,0,125,21,1,
        0,0,0,126,129,3,20,10,0,127,129,3,4,2,0,128,126,1,0,0,0,128,127,
        1,0,0,0,129,23,1,0,0,0,130,131,5,6,0,0,131,132,5,13,0,0,132,133,
        3,42,21,0,133,134,5,14,0,0,134,135,3,22,11,0,135,25,1,0,0,0,136,
        137,5,8,0,0,137,138,5,13,0,0,138,139,3,42,21,0,139,140,5,14,0,0,
        140,143,3,22,11,0,141,142,5,9,0,0,142,144,3,22,11,0,143,141,1,0,
        0,0,143,144,1,0,0,0,144,27,1,0,0,0,145,146,5,7,0,0,146,148,5,13,
        0,0,147,149,3,14,7,0,148,147,1,0,0,0,148,149,1,0,0,0,149,150,1,0,
        0,0,150,151,3,10,5,0,151,152,1,0,0,0,152,153,5,15,0,0,153,154,3,
        42,21,0,154,155,5,15,0,0,155,156,3,30,15,0,156,157,5,14,0,0,157,
        158,3,22,11,0,158,29,1,0,0,0,159,160,5,33,0,0,160,161,5,20,0,0,161,
        162,3,42,21,0,162,31,1,0,0,0,163,164,3,30,15,0,164,165,5,15,0,0,
        165,33,1,0,0,0,166,167,5,10,0,0,167,170,3,42,21,0,168,170,5,10,0,
        0,169,166,1,0,0,0,169,168,1,0,0,0,170,35,1,0,0,0,171,176,3,42,21,
        0,172,173,5,18,0,0,173,175,3,42,21,0,174,172,1,0,0,0,175,178,1,0,
        0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,180,1,0,0,0,178,176,1,0,
        0,0,179,171,1,0,0,0,179,180,1,0,0,0,180,37,1,0,0,0,181,182,5,33,
        0,0,182,183,5,13,0,0,183,184,3,36,18,0,184,185,5,14,0,0,185,39,1,
        0,0,0,186,187,3,38,19,0,187,188,5,15,0,0,188,41,1,0,0,0,189,190,
        6,21,-1,0,190,191,3,44,22,0,191,209,1,0,0,0,192,193,10,6,0,0,193,
        194,7,1,0,0,194,208,3,42,21,7,195,196,10,5,0,0,196,197,7,2,0,0,197,
        208,3,42,21,6,198,199,10,4,0,0,199,200,7,3,0,0,200,208,3,42,21,5,
        201,202,10,3,0,0,202,203,5,32,0,0,203,208,3,42,21,4,204,205,10,2,
        0,0,205,206,5,31,0,0,206,208,3,42,21,3,207,192,1,0,0,0,207,195,1,
        0,0,0,207,198,1,0,0,0,207,201,1,0,0,0,207,204,1,0,0,0,208,211,1,
        0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,43,1,0,0,0,211,209,1,0,
        0,0,212,223,5,34,0,0,213,223,5,35,0,0,214,223,5,11,0,0,215,223,5,
        12,0,0,216,223,5,33,0,0,217,223,3,38,19,0,218,219,5,13,0,0,219,220,
        3,42,21,0,220,221,5,14,0,0,221,223,1,0,0,0,222,212,1,0,0,0,222,213,
        1,0,0,0,222,214,1,0,0,0,222,215,1,0,0,0,222,216,1,0,0,0,222,217,
        1,0,0,0,222,218,1,0,0,0,223,45,1,0,0,0,19,52,66,77,81,87,91,96,105,
        117,120,128,143,148,169,176,179,207,209,222
    ]

class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'bool'", "'float'", "'double'", 
                     "'void'", "'while'", "'for'", "'if'", "'else'", "'return'", 
                     "'TRUE'", "'FALSE'", "'('", "')'", "';'", "'{'", "'}'", 
                     "','", "'.'", "'='", "'=='", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'>'", "'<'", "'>='", "'<='", "'||'", "'&&'" ]

    symbolicNames = [ "<INVALID>", "INT", "BOOL", "FLOAT", "DOUBLE", "VOID", 
                      "WHILE", "FOR", "IF", "ELSE", "RETURN", "TRUE", "FALSE", 
                      "PA", "PC", "PYC", "LLA", "LLC", "COMA", "PUNTO", 
                      "ASIG", "IGUAL", "SUMA", "RESTA", "MULT", "DIV", "MOD", 
                      "MAY", "MEN", "MAYI", "MENI", "OR", "AND", "ID", "NUMERO", 
                      "DECIMAL", "WS", "COMENTARIO" ]

    RULE_programa = 0
    RULE_instrucciones = 1
    RULE_instruccion = 2
    RULE_declaracionGlobal = 3
    RULE_restoDeclaracion = 4
    RULE_decItem = 5
    RULE_funcionVoid = 6
    RULE_tipoDatos = 7
    RULE_argumento = 8
    RULE_argumentos = 9
    RULE_bloque = 10
    RULE_instruccionOBloque = 11
    RULE_iwhile = 12
    RULE_iif = 13
    RULE_ifor = 14
    RULE_asignacion = 15
    RULE_asignacionPYC = 16
    RULE_returnfun = 17
    RULE_ids = 18
    RULE_funcionVar = 19
    RULE_llamadafun = 20
    RULE_exp = 21
    RULE_factor = 22

    ruleNames =  [ "programa", "instrucciones", "instruccion", "declaracionGlobal", 
                   "restoDeclaracion", "decItem", "funcionVoid", "tipoDatos", 
                   "argumento", "argumentos", "bloque", "instruccionOBloque", 
                   "iwhile", "iif", "ifor", "asignacion", "asignacionPYC", 
                   "returnfun", "ids", "funcionVar", "llamadafun", "exp", 
                   "factor" ]

    EOF = Token.EOF
    INT=1
    BOOL=2
    FLOAT=3
    DOUBLE=4
    VOID=5
    WHILE=6
    FOR=7
    IF=8
    ELSE=9
    RETURN=10
    TRUE=11
    FALSE=12
    PA=13
    PC=14
    PYC=15
    LLA=16
    LLC=17
    COMA=18
    PUNTO=19
    ASIG=20
    IGUAL=21
    SUMA=22
    RESTA=23
    MULT=24
    DIV=25
    MOD=26
    MAY=27
    MEN=28
    MAYI=29
    MENI=30
    OR=31
    AND=32
    ID=33
    NUMERO=34
    DECIMAL=35
    WS=36
    COMENTARIO=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def EOF(self):
            return self.getToken(compiladoresParser.EOF, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = compiladoresParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.instrucciones()
            self.state = 47
            self.match(compiladoresParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.InstruccionContext,i)


        def getRuleIndex(self):
            return compiladoresParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = compiladoresParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8590001662) != 0):
                self.state = 49
                self.instruccion()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionGlobal(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionGlobalContext,0)


        def funcionVoid(self):
            return self.getTypedRuleContext(compiladoresParser.FuncionVoidContext,0)


        def iwhile(self):
            return self.getTypedRuleContext(compiladoresParser.IwhileContext,0)


        def ifor(self):
            return self.getTypedRuleContext(compiladoresParser.IforContext,0)


        def iif(self):
            return self.getTypedRuleContext(compiladoresParser.IifContext,0)


        def asignacionPYC(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionPYCContext,0)


        def returnfun(self):
            return self.getTypedRuleContext(compiladoresParser.ReturnfunContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def llamadafun(self):
            return self.getTypedRuleContext(compiladoresParser.LlamadafunContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = compiladoresParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruccion)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.declaracionGlobal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.funcionVoid()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.iwhile()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.ifor()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 59
                self.iif()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 60
                self.asignacionPYC()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 61
                self.returnfun()
                self.state = 62
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 64
                self.llamadafun()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 65
                self.bloque()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionGlobalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipoDatos(self):
            return self.getTypedRuleContext(compiladoresParser.TipoDatosContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def restoDeclaracion(self):
            return self.getTypedRuleContext(compiladoresParser.RestoDeclaracionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_declaracionGlobal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionGlobal" ):
                listener.enterDeclaracionGlobal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionGlobal" ):
                listener.exitDeclaracionGlobal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionGlobal" ):
                return visitor.visitDeclaracionGlobal(self)
            else:
                return visitor.visitChildren(self)




    def declaracionGlobal(self):

        localctx = compiladoresParser.DeclaracionGlobalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracionGlobal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.tipoDatos()
            self.state = 69
            self.match(compiladoresParser.ID)
            self.state = 70
            self.restoDeclaracion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RestoDeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def argumentos(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentosContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.COMA)
            else:
                return self.getToken(compiladoresParser.COMA, i)

        def decItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.DecItemContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.DecItemContext,i)


        def getRuleIndex(self):
            return compiladoresParser.RULE_restoDeclaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRestoDeclaracion" ):
                listener.enterRestoDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRestoDeclaracion" ):
                listener.exitRestoDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRestoDeclaracion" ):
                return visitor.visitRestoDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def restoDeclaracion(self):

        localctx = compiladoresParser.RestoDeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_restoDeclaracion)
        self._la = 0 # Token type
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(compiladoresParser.PA)
                self.state = 73
                self.argumentos()
                self.state = 74
                self.match(compiladoresParser.PC)
                self.state = 77
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [16]:
                    self.state = 75
                    self.bloque()
                    pass
                elif token in [15]:
                    self.state = 76
                    self.match(compiladoresParser.PYC)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [15, 18, 20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 79
                    self.match(compiladoresParser.ASIG)
                    self.state = 80
                    self.exp(0)


                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==18:
                    self.state = 83
                    self.match(compiladoresParser.COMA)
                    self.state = 84
                    self.decItem()
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 90
                self.match(compiladoresParser.PYC)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_decItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecItem" ):
                listener.enterDecItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecItem" ):
                listener.exitDecItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecItem" ):
                return visitor.visitDecItem(self)
            else:
                return visitor.visitChildren(self)




    def decItem(self):

        localctx = compiladoresParser.DecItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_decItem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(compiladoresParser.ID)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 94
                self.match(compiladoresParser.ASIG)
                self.state = 95
                self.exp(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionVoidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(compiladoresParser.VOID, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def argumentos(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentosContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_funcionVoid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncionVoid" ):
                listener.enterFuncionVoid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncionVoid" ):
                listener.exitFuncionVoid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncionVoid" ):
                return visitor.visitFuncionVoid(self)
            else:
                return visitor.visitChildren(self)




    def funcionVoid(self):

        localctx = compiladoresParser.FuncionVoidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcionVoid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(compiladoresParser.VOID)
            self.state = 99
            self.match(compiladoresParser.ID)
            self.state = 100
            self.match(compiladoresParser.PA)
            self.state = 101
            self.argumentos()
            self.state = 102
            self.match(compiladoresParser.PC)
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 103
                self.bloque()
                pass
            elif token in [15]:
                self.state = 104
                self.match(compiladoresParser.PYC)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoDatosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(compiladoresParser.BOOL, 0)

        def INT(self):
            return self.getToken(compiladoresParser.INT, 0)

        def FLOAT(self):
            return self.getToken(compiladoresParser.FLOAT, 0)

        def DOUBLE(self):
            return self.getToken(compiladoresParser.DOUBLE, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_tipoDatos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoDatos" ):
                listener.enterTipoDatos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoDatos" ):
                listener.exitTipoDatos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoDatos" ):
                return visitor.visitTipoDatos(self)
            else:
                return visitor.visitChildren(self)




    def tipoDatos(self):

        localctx = compiladoresParser.TipoDatosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tipoDatos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipoDatos(self):
            return self.getTypedRuleContext(compiladoresParser.TipoDatosContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_argumento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumento" ):
                listener.enterArgumento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumento" ):
                listener.exitArgumento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumento" ):
                return visitor.visitArgumento(self)
            else:
                return visitor.visitChildren(self)




    def argumento(self):

        localctx = compiladoresParser.ArgumentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_argumento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.tipoDatos()
            self.state = 110
            self.match(compiladoresParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argumento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.ArgumentoContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.ArgumentoContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.COMA)
            else:
                return self.getToken(compiladoresParser.COMA, i)

        def getRuleIndex(self):
            return compiladoresParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = compiladoresParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                self.state = 112
                self.argumento()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==18:
                    self.state = 113
                    self.match(compiladoresParser.COMA)
                    self.state = 114
                    self.argumento()
                    self.state = 119
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLA(self):
            return self.getToken(compiladoresParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def LLC(self):
            return self.getToken(compiladoresParser.LLC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = compiladoresParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(compiladoresParser.LLA)
            self.state = 123
            self.instrucciones()
            self.state = 124
            self.match(compiladoresParser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionOBloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_instruccionOBloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccionOBloque" ):
                listener.enterInstruccionOBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccionOBloque" ):
                listener.exitInstruccionOBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionOBloque" ):
                return visitor.visitInstruccionOBloque(self)
            else:
                return visitor.visitChildren(self)




    def instruccionOBloque(self):

        localctx = compiladoresParser.InstruccionOBloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_instruccionOBloque)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.bloque()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.instruccion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IwhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(compiladoresParser.WHILE, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccionOBloque(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionOBloqueContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_iwhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIwhile" ):
                listener.enterIwhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIwhile" ):
                listener.exitIwhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIwhile" ):
                return visitor.visitIwhile(self)
            else:
                return visitor.visitChildren(self)




    def iwhile(self):

        localctx = compiladoresParser.IwhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(compiladoresParser.WHILE)
            self.state = 131
            self.match(compiladoresParser.PA)
            self.state = 132
            self.exp(0)
            self.state = 133
            self.match(compiladoresParser.PC)
            self.state = 134
            self.instruccionOBloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(compiladoresParser.IF, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccionOBloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.InstruccionOBloqueContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.InstruccionOBloqueContext,i)


        def ELSE(self):
            return self.getToken(compiladoresParser.ELSE, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_iif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIif" ):
                listener.enterIif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIif" ):
                listener.exitIif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIif" ):
                return visitor.visitIif(self)
            else:
                return visitor.visitChildren(self)




    def iif(self):

        localctx = compiladoresParser.IifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_iif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(compiladoresParser.IF)
            self.state = 137
            self.match(compiladoresParser.PA)
            self.state = 138
            self.exp(0)
            self.state = 139
            self.match(compiladoresParser.PC)
            self.state = 140
            self.instruccionOBloque()
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 141
                self.match(compiladoresParser.ELSE)
                self.state = 142
                self.instruccionOBloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(compiladoresParser.FOR, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def PYC(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.PYC)
            else:
                return self.getToken(compiladoresParser.PYC, i)

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccionOBloque(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionOBloqueContext,0)


        def decItem(self):
            return self.getTypedRuleContext(compiladoresParser.DecItemContext,0)


        def tipoDatos(self):
            return self.getTypedRuleContext(compiladoresParser.TipoDatosContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_ifor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfor" ):
                listener.enterIfor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfor" ):
                listener.exitIfor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfor" ):
                return visitor.visitIfor(self)
            else:
                return visitor.visitChildren(self)




    def ifor(self):

        localctx = compiladoresParser.IforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ifor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(compiladoresParser.FOR)
            self.state = 146
            self.match(compiladoresParser.PA)

            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                self.state = 147
                self.tipoDatos()


            self.state = 150
            self.decItem()
            self.state = 152
            self.match(compiladoresParser.PYC)
            self.state = 153
            self.exp(0)
            self.state = 154
            self.match(compiladoresParser.PYC)
            self.state = 155
            self.asignacion()
            self.state = 156
            self.match(compiladoresParser.PC)
            self.state = 157
            self.instruccionOBloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = compiladoresParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(compiladoresParser.ID)
            self.state = 160
            self.match(compiladoresParser.ASIG)
            self.state = 161
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionPYCContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_asignacionPYC

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacionPYC" ):
                listener.enterAsignacionPYC(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacionPYC" ):
                listener.exitAsignacionPYC(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacionPYC" ):
                return visitor.visitAsignacionPYC(self)
            else:
                return visitor.visitChildren(self)




    def asignacionPYC(self):

        localctx = compiladoresParser.AsignacionPYCContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_asignacionPYC)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.asignacion()
            self.state = 164
            self.match(compiladoresParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnfunContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(compiladoresParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_returnfun

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnfun" ):
                listener.enterReturnfun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnfun" ):
                listener.exitReturnfun(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnfun" ):
                return visitor.visitReturnfun(self)
            else:
                return visitor.visitChildren(self)




    def returnfun(self):

        localctx = compiladoresParser.ReturnfunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_returnfun)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(compiladoresParser.RETURN)
                self.state = 167
                self.exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(compiladoresParser.RETURN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.ExpContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.ExpContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.COMA)
            else:
                return self.getToken(compiladoresParser.COMA, i)

        def getRuleIndex(self):
            return compiladoresParser.RULE_ids

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIds" ):
                listener.enterIds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIds" ):
                listener.exitIds(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds" ):
                return visitor.visitIds(self)
            else:
                return visitor.visitChildren(self)




    def ids(self):

        localctx = compiladoresParser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ids)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 60129556480) != 0):
                self.state = 171
                self.exp(0)
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==18:
                    self.state = 172
                    self.match(compiladoresParser.COMA)
                    self.state = 173
                    self.exp(0)
                    self.state = 178
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionVarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def ids(self):
            return self.getTypedRuleContext(compiladoresParser.IdsContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_funcionVar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncionVar" ):
                listener.enterFuncionVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncionVar" ):
                listener.exitFuncionVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncionVar" ):
                return visitor.visitFuncionVar(self)
            else:
                return visitor.visitChildren(self)




    def funcionVar(self):

        localctx = compiladoresParser.FuncionVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_funcionVar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(compiladoresParser.ID)
            self.state = 182
            self.match(compiladoresParser.PA)
            self.state = 183
            self.ids()
            self.state = 184
            self.match(compiladoresParser.PC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadafunContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcionVar(self):
            return self.getTypedRuleContext(compiladoresParser.FuncionVarContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_llamadafun

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamadafun" ):
                listener.enterLlamadafun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamadafun" ):
                listener.exitLlamadafun(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadafun" ):
                return visitor.visitLlamadafun(self)
            else:
                return visitor.visitChildren(self)




    def llamadafun(self):

        localctx = compiladoresParser.LlamadafunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_llamadafun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.funcionVar()
            self.state = 187
            self.match(compiladoresParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.ExpContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.ExpContext,i)


        def MULT(self):
            return self.getToken(compiladoresParser.MULT, 0)

        def DIV(self):
            return self.getToken(compiladoresParser.DIV, 0)

        def MOD(self):
            return self.getToken(compiladoresParser.MOD, 0)

        def SUMA(self):
            return self.getToken(compiladoresParser.SUMA, 0)

        def RESTA(self):
            return self.getToken(compiladoresParser.RESTA, 0)

        def MAY(self):
            return self.getToken(compiladoresParser.MAY, 0)

        def MEN(self):
            return self.getToken(compiladoresParser.MEN, 0)

        def MAYI(self):
            return self.getToken(compiladoresParser.MAYI, 0)

        def IGUAL(self):
            return self.getToken(compiladoresParser.IGUAL, 0)

        def AND(self):
            return self.getToken(compiladoresParser.AND, 0)

        def OR(self):
            return self.getToken(compiladoresParser.OR, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = compiladoresParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 209
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 207
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = compiladoresParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 192
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 193
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 194
                        self.exp(7)
                        pass

                    elif la_ == 2:
                        localctx = compiladoresParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 195
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 196
                        _la = self._input.LA(1)
                        if not(_la==22 or _la==23):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 197
                        self.exp(6)
                        pass

                    elif la_ == 3:
                        localctx = compiladoresParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 198
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 199
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 941621248) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 200
                        self.exp(5)
                        pass

                    elif la_ == 4:
                        localctx = compiladoresParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 201
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 202
                        self.match(compiladoresParser.AND)
                        self.state = 203
                        self.exp(4)
                        pass

                    elif la_ == 5:
                        localctx = compiladoresParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 204
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 205
                        self.match(compiladoresParser.OR)
                        self.state = 206
                        self.exp(3)
                        pass

             
                self.state = 211
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def DECIMAL(self):
            return self.getToken(compiladoresParser.DECIMAL, 0)

        def TRUE(self):
            return self.getToken(compiladoresParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(compiladoresParser.FALSE, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def funcionVar(self):
            return self.getTypedRuleContext(compiladoresParser.FuncionVarContext,0)


        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = compiladoresParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_factor)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.match(compiladoresParser.DECIMAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
                self.match(compiladoresParser.TRUE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 215
                self.match(compiladoresParser.FALSE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 216
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 217
                self.funcionVar()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 218
                self.match(compiladoresParser.PA)
                self.state = 219
                self.exp(0)
                self.state = 220
                self.match(compiladoresParser.PC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




