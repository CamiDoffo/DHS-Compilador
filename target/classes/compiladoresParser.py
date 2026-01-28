# Generated from src/main/antlr4/compiladores.g4 by ANTLR 4.13.2
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
        4,1,37,290,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,0,1,1,5,1,79,8,1,10,
        1,12,1,82,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,95,
        8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,108,8,4,1,5,
        1,5,5,5,112,8,5,10,5,12,5,115,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,5,10,138,
        8,10,10,10,12,10,141,9,10,3,10,143,8,10,1,11,1,11,1,11,1,11,1,12,
        1,12,1,12,1,12,5,12,153,8,12,10,12,12,12,156,9,12,1,13,1,13,1,13,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,169,8,14,1,15,1,15,
        1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,3,17,181,8,17,1,18,1,18,
        1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,
        1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,219,8,24,1,25,1,25,
        1,25,3,25,224,8,25,1,26,1,26,1,26,5,26,229,8,26,10,26,12,26,232,
        9,26,3,26,234,8,26,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,29,
        1,29,5,29,246,8,29,10,29,12,29,249,9,29,1,30,1,30,1,30,1,31,1,31,
        5,31,256,8,31,10,31,12,31,259,9,31,1,32,1,32,1,32,1,33,1,33,1,33,
        1,33,1,33,1,33,1,33,1,33,3,33,272,8,33,1,34,1,34,1,34,1,34,1,35,
        1,35,1,35,5,35,281,8,35,10,35,12,35,284,9,35,1,36,1,36,3,36,288,
        8,36,1,36,0,0,37,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,0,7,1,0,
        1,4,1,0,22,25,1,0,22,23,1,0,24,26,2,0,21,21,27,30,1,0,11,12,1,0,
        31,32,281,0,74,1,0,0,0,2,80,1,0,0,0,4,94,1,0,0,0,6,96,1,0,0,0,8,
        107,1,0,0,0,10,113,1,0,0,0,12,118,1,0,0,0,14,122,1,0,0,0,16,129,
        1,0,0,0,18,131,1,0,0,0,20,142,1,0,0,0,22,144,1,0,0,0,24,148,1,0,
        0,0,26,157,1,0,0,0,28,168,1,0,0,0,30,170,1,0,0,0,32,174,1,0,0,0,
        34,180,1,0,0,0,36,182,1,0,0,0,38,185,1,0,0,0,40,191,1,0,0,0,42,201,
        1,0,0,0,44,203,1,0,0,0,46,208,1,0,0,0,48,211,1,0,0,0,50,223,1,0,
        0,0,52,233,1,0,0,0,54,235,1,0,0,0,56,240,1,0,0,0,58,243,1,0,0,0,
        60,250,1,0,0,0,62,253,1,0,0,0,64,260,1,0,0,0,66,271,1,0,0,0,68,273,
        1,0,0,0,70,277,1,0,0,0,72,287,1,0,0,0,74,75,3,2,1,0,75,76,5,0,0,
        1,76,1,1,0,0,0,77,79,3,4,2,0,78,77,1,0,0,0,79,82,1,0,0,0,80,78,1,
        0,0,0,80,81,1,0,0,0,81,3,1,0,0,0,82,80,1,0,0,0,83,95,3,6,3,0,84,
        95,3,14,7,0,85,95,3,38,19,0,86,95,3,40,20,0,87,95,3,48,24,0,88,95,
        3,36,18,0,89,90,3,50,25,0,90,91,5,15,0,0,91,95,1,0,0,0,92,95,3,56,
        28,0,93,95,3,22,11,0,94,83,1,0,0,0,94,84,1,0,0,0,94,85,1,0,0,0,94,
        86,1,0,0,0,94,87,1,0,0,0,94,88,1,0,0,0,94,89,1,0,0,0,94,92,1,0,0,
        0,94,93,1,0,0,0,95,5,1,0,0,0,96,97,3,16,8,0,97,98,5,33,0,0,98,99,
        3,8,4,0,99,7,1,0,0,0,100,101,5,13,0,0,101,102,3,20,10,0,102,103,
        5,14,0,0,103,104,3,22,11,0,104,108,1,0,0,0,105,108,3,10,5,0,106,
        108,3,12,6,0,107,100,1,0,0,0,107,105,1,0,0,0,107,106,1,0,0,0,108,
        9,1,0,0,0,109,110,5,18,0,0,110,112,5,33,0,0,111,109,1,0,0,0,112,
        115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,116,1,0,0,0,115,
        113,1,0,0,0,116,117,5,15,0,0,117,11,1,0,0,0,118,119,5,20,0,0,119,
        120,3,58,29,0,120,121,5,15,0,0,121,13,1,0,0,0,122,123,5,5,0,0,123,
        124,5,33,0,0,124,125,5,13,0,0,125,126,3,20,10,0,126,127,5,14,0,0,
        127,128,3,22,11,0,128,15,1,0,0,0,129,130,7,0,0,0,130,17,1,0,0,0,
        131,132,3,16,8,0,132,133,5,33,0,0,133,19,1,0,0,0,134,139,3,18,9,
        0,135,136,5,18,0,0,136,138,3,18,9,0,137,135,1,0,0,0,138,141,1,0,
        0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,143,1,0,0,0,141,139,1,0,
        0,0,142,134,1,0,0,0,142,143,1,0,0,0,143,21,1,0,0,0,144,145,5,16,
        0,0,145,146,3,2,1,0,146,147,5,17,0,0,147,23,1,0,0,0,148,149,3,16,
        8,0,149,154,5,33,0,0,150,151,5,18,0,0,151,153,5,33,0,0,152,150,1,
        0,0,0,153,156,1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,25,1,0,
        0,0,156,154,1,0,0,0,157,158,3,24,12,0,158,159,5,15,0,0,159,27,1,
        0,0,0,160,161,3,16,8,0,161,162,3,30,15,0,162,163,5,15,0,0,163,169,
        1,0,0,0,164,165,3,16,8,0,165,166,3,32,16,0,166,167,5,15,0,0,167,
        169,1,0,0,0,168,160,1,0,0,0,168,164,1,0,0,0,169,29,1,0,0,0,170,171,
        5,33,0,0,171,172,5,20,0,0,172,173,3,58,29,0,173,31,1,0,0,0,174,175,
        5,33,0,0,175,176,5,20,0,0,176,177,3,70,35,0,177,33,1,0,0,0,178,181,
        3,30,15,0,179,181,3,32,16,0,180,178,1,0,0,0,180,179,1,0,0,0,181,
        35,1,0,0,0,182,183,3,34,17,0,183,184,5,15,0,0,184,37,1,0,0,0,185,
        186,5,6,0,0,186,187,5,13,0,0,187,188,3,72,36,0,188,189,5,14,0,0,
        189,190,3,22,11,0,190,39,1,0,0,0,191,192,5,7,0,0,192,193,5,13,0,
        0,193,194,3,42,21,0,194,195,5,15,0,0,195,196,3,72,36,0,196,197,5,
        15,0,0,197,198,3,44,22,0,198,199,5,14,0,0,199,200,3,22,11,0,200,
        41,1,0,0,0,201,202,3,30,15,0,202,43,1,0,0,0,203,204,5,33,0,0,204,
        205,5,20,0,0,205,206,5,33,0,0,206,207,3,46,23,0,207,45,1,0,0,0,208,
        209,7,1,0,0,209,210,5,34,0,0,210,47,1,0,0,0,211,212,5,8,0,0,212,
        213,5,13,0,0,213,214,3,72,36,0,214,215,5,14,0,0,215,218,3,22,11,
        0,216,217,5,9,0,0,217,219,3,22,11,0,218,216,1,0,0,0,218,219,1,0,
        0,0,219,49,1,0,0,0,220,221,5,10,0,0,221,224,3,58,29,0,222,224,5,
        10,0,0,223,220,1,0,0,0,223,222,1,0,0,0,224,51,1,0,0,0,225,230,3,
        58,29,0,226,227,5,18,0,0,227,229,3,58,29,0,228,226,1,0,0,0,229,232,
        1,0,0,0,230,228,1,0,0,0,230,231,1,0,0,0,231,234,1,0,0,0,232,230,
        1,0,0,0,233,225,1,0,0,0,233,234,1,0,0,0,234,53,1,0,0,0,235,236,5,
        33,0,0,236,237,5,13,0,0,237,238,3,52,26,0,238,239,5,14,0,0,239,55,
        1,0,0,0,240,241,3,54,27,0,241,242,5,15,0,0,242,57,1,0,0,0,243,247,
        3,62,31,0,244,246,3,60,30,0,245,244,1,0,0,0,246,249,1,0,0,0,247,
        245,1,0,0,0,247,248,1,0,0,0,248,59,1,0,0,0,249,247,1,0,0,0,250,251,
        7,2,0,0,251,252,3,62,31,0,252,61,1,0,0,0,253,257,3,66,33,0,254,256,
        3,64,32,0,255,254,1,0,0,0,256,259,1,0,0,0,257,255,1,0,0,0,257,258,
        1,0,0,0,258,63,1,0,0,0,259,257,1,0,0,0,260,261,7,3,0,0,261,262,3,
        66,33,0,262,65,1,0,0,0,263,272,5,34,0,0,264,272,5,35,0,0,265,272,
        5,33,0,0,266,272,3,54,27,0,267,268,5,13,0,0,268,269,3,58,29,0,269,
        270,5,14,0,0,270,272,1,0,0,0,271,263,1,0,0,0,271,264,1,0,0,0,271,
        265,1,0,0,0,271,266,1,0,0,0,271,267,1,0,0,0,272,67,1,0,0,0,273,274,
        5,33,0,0,274,275,7,4,0,0,275,276,3,66,33,0,276,69,1,0,0,0,277,282,
        7,5,0,0,278,279,7,6,0,0,279,281,7,5,0,0,280,278,1,0,0,0,281,284,
        1,0,0,0,282,280,1,0,0,0,282,283,1,0,0,0,283,71,1,0,0,0,284,282,1,
        0,0,0,285,288,3,68,34,0,286,288,3,70,35,0,287,285,1,0,0,0,287,286,
        1,0,0,0,288,73,1,0,0,0,18,80,94,107,113,139,142,154,168,180,218,
        223,230,233,247,257,271,282,287
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
    RULE_listaVars = 5
    RULE_asignacionInit = 6
    RULE_funcionVoid = 7
    RULE_tipoDatos = 8
    RULE_argumento = 9
    RULE_argumentos = 10
    RULE_bloque = 11
    RULE_declaracion = 12
    RULE_declaracionPYC = 13
    RULE_inic = 14
    RULE_asignacionNum = 15
    RULE_asignacionBool = 16
    RULE_asignacion = 17
    RULE_asignacionPYC = 18
    RULE_iwhile = 19
    RULE_ifor = 20
    RULE_init = 21
    RULE_iter = 22
    RULE_iteracion = 23
    RULE_iif = 24
    RULE_returnfun = 25
    RULE_ids = 26
    RULE_funcionVar = 27
    RULE_llamadafun = 28
    RULE_exp = 29
    RULE_expPrima = 30
    RULE_term = 31
    RULE_t = 32
    RULE_factor = 33
    RULE_opcomp = 34
    RULE_opbool = 35
    RULE_cond = 36

    ruleNames =  [ "programa", "instrucciones", "instruccion", "declaracionGlobal", 
                   "restoDeclaracion", "listaVars", "asignacionInit", "funcionVoid", 
                   "tipoDatos", "argumento", "argumentos", "bloque", "declaracion", 
                   "declaracionPYC", "inic", "asignacionNum", "asignacionBool", 
                   "asignacion", "asignacionPYC", "iwhile", "ifor", "init", 
                   "iter", "iteracion", "iif", "returnfun", "ids", "funcionVar", 
                   "llamadafun", "exp", "expPrima", "term", "t", "factor", 
                   "opcomp", "opbool", "cond" ]

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
        self.checkVersion("4.13.2")
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
            self.state = 74
            self.instrucciones()
            self.state = 75
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
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8590001662) != 0):
                self.state = 77
                self.instruccion()
                self.state = 82
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
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.declaracionGlobal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.funcionVoid()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.iwhile()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.ifor()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 87
                self.iif()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 88
                self.asignacionPYC()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 89
                self.returnfun()
                self.state = 90
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 92
                self.llamadafun()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 93
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
            self.state = 96
            self.tipoDatos()
            self.state = 97
            self.match(compiladoresParser.ID)
            self.state = 98
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


        def listaVars(self):
            return self.getTypedRuleContext(compiladoresParser.ListaVarsContext,0)


        def asignacionInit(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionInitContext,0)


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
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.match(compiladoresParser.PA)
                self.state = 101
                self.argumentos()
                self.state = 102
                self.match(compiladoresParser.PC)
                self.state = 103
                self.bloque()
                pass
            elif token in [15, 18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.listaVars()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.asignacionInit()
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


    class ListaVarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.COMA)
            else:
                return self.getToken(compiladoresParser.COMA, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.ID)
            else:
                return self.getToken(compiladoresParser.ID, i)

        def getRuleIndex(self):
            return compiladoresParser.RULE_listaVars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaVars" ):
                listener.enterListaVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaVars" ):
                listener.exitListaVars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaVars" ):
                return visitor.visitListaVars(self)
            else:
                return visitor.visitChildren(self)




    def listaVars(self):

        localctx = compiladoresParser.ListaVarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_listaVars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 109
                self.match(compiladoresParser.COMA)
                self.state = 110
                self.match(compiladoresParser.ID)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            self.match(compiladoresParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_asignacionInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacionInit" ):
                listener.enterAsignacionInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacionInit" ):
                listener.exitAsignacionInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacionInit" ):
                return visitor.visitAsignacionInit(self)
            else:
                return visitor.visitChildren(self)




    def asignacionInit(self):

        localctx = compiladoresParser.AsignacionInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_asignacionInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(compiladoresParser.ASIG)
            self.state = 119
            self.exp()
            self.state = 120
            self.match(compiladoresParser.PYC)
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
        self.enterRule(localctx, 14, self.RULE_funcionVoid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(compiladoresParser.VOID)
            self.state = 123
            self.match(compiladoresParser.ID)
            self.state = 124
            self.match(compiladoresParser.PA)
            self.state = 125
            self.argumentos()
            self.state = 126
            self.match(compiladoresParser.PC)
            self.state = 127
            self.bloque()
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
        self.enterRule(localctx, 16, self.RULE_tipoDatos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
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
        self.enterRule(localctx, 18, self.RULE_argumento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.tipoDatos()
            self.state = 132
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
        self.enterRule(localctx, 20, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                self.state = 134
                self.argumento()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==18:
                    self.state = 135
                    self.match(compiladoresParser.COMA)
                    self.state = 136
                    self.argumento()
                    self.state = 141
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
        self.enterRule(localctx, 22, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(compiladoresParser.LLA)
            self.state = 145
            self.instrucciones()
            self.state = 146
            self.match(compiladoresParser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipoDatos(self):
            return self.getTypedRuleContext(compiladoresParser.TipoDatosContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.ID)
            else:
                return self.getToken(compiladoresParser.ID, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.COMA)
            else:
                return self.getToken(compiladoresParser.COMA, i)

        def getRuleIndex(self):
            return compiladoresParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = compiladoresParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_declaracion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.tipoDatos()
            self.state = 149
            self.match(compiladoresParser.ID)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 150
                self.match(compiladoresParser.COMA)
                self.state = 151
                self.match(compiladoresParser.ID)
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionPYCContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_declaracionPYC

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionPYC" ):
                listener.enterDeclaracionPYC(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionPYC" ):
                listener.exitDeclaracionPYC(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionPYC" ):
                return visitor.visitDeclaracionPYC(self)
            else:
                return visitor.visitChildren(self)




    def declaracionPYC(self):

        localctx = compiladoresParser.DeclaracionPYCContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_declaracionPYC)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.declaracion()
            self.state = 158
            self.match(compiladoresParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipoDatos(self):
            return self.getTypedRuleContext(compiladoresParser.TipoDatosContext,0)


        def asignacionNum(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionNumContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def asignacionBool(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionBoolContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_inic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInic" ):
                listener.enterInic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInic" ):
                listener.exitInic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInic" ):
                return visitor.visitInic(self)
            else:
                return visitor.visitChildren(self)




    def inic(self):

        localctx = compiladoresParser.InicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_inic)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.tipoDatos()
                self.state = 161
                self.asignacionNum()
                self.state = 162
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.tipoDatos()
                self.state = 165
                self.asignacionBool()
                self.state = 166
                self.match(compiladoresParser.PYC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionNumContext(ParserRuleContext):
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
            return compiladoresParser.RULE_asignacionNum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacionNum" ):
                listener.enterAsignacionNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacionNum" ):
                listener.exitAsignacionNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacionNum" ):
                return visitor.visitAsignacionNum(self)
            else:
                return visitor.visitChildren(self)




    def asignacionNum(self):

        localctx = compiladoresParser.AsignacionNumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_asignacionNum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(compiladoresParser.ID)
            self.state = 171
            self.match(compiladoresParser.ASIG)
            self.state = 172
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionBoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def opbool(self):
            return self.getTypedRuleContext(compiladoresParser.OpboolContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_asignacionBool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacionBool" ):
                listener.enterAsignacionBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacionBool" ):
                listener.exitAsignacionBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacionBool" ):
                return visitor.visitAsignacionBool(self)
            else:
                return visitor.visitChildren(self)




    def asignacionBool(self):

        localctx = compiladoresParser.AsignacionBoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_asignacionBool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(compiladoresParser.ID)
            self.state = 175
            self.match(compiladoresParser.ASIG)
            self.state = 176
            self.opbool()
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

        def asignacionNum(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionNumContext,0)


        def asignacionBool(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionBoolContext,0)


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
        self.enterRule(localctx, 34, self.RULE_asignacion)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.asignacionNum()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.asignacionBool()
                pass


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
        self.enterRule(localctx, 36, self.RULE_asignacionPYC)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.asignacion()
            self.state = 183
            self.match(compiladoresParser.PYC)
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

        def cond(self):
            return self.getTypedRuleContext(compiladoresParser.CondContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


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
        self.enterRule(localctx, 38, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(compiladoresParser.WHILE)
            self.state = 186
            self.match(compiladoresParser.PA)
            self.state = 187
            self.cond()
            self.state = 188
            self.match(compiladoresParser.PC)
            self.state = 189
            self.bloque()
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

        def init(self):
            return self.getTypedRuleContext(compiladoresParser.InitContext,0)


        def PYC(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.PYC)
            else:
                return self.getToken(compiladoresParser.PYC, i)

        def cond(self):
            return self.getTypedRuleContext(compiladoresParser.CondContext,0)


        def iter_(self):
            return self.getTypedRuleContext(compiladoresParser.IterContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


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
        self.enterRule(localctx, 40, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(compiladoresParser.FOR)
            self.state = 192
            self.match(compiladoresParser.PA)
            self.state = 193
            self.init()
            self.state = 194
            self.match(compiladoresParser.PYC)
            self.state = 195
            self.cond()
            self.state = 196
            self.match(compiladoresParser.PYC)
            self.state = 197
            self.iter_()
            self.state = 198
            self.match(compiladoresParser.PC)
            self.state = 199
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacionNum(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionNumContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit" ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit" ):
                listener.exitInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = compiladoresParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.asignacionNum()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.ID)
            else:
                return self.getToken(compiladoresParser.ID, i)

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def iteracion(self):
            return self.getTypedRuleContext(compiladoresParser.IteracionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_iter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIter" ):
                listener.enterIter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIter" ):
                listener.exitIter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIter" ):
                return visitor.visitIter(self)
            else:
                return visitor.visitChildren(self)




    def iter_(self):

        localctx = compiladoresParser.IterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_iter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(compiladoresParser.ID)
            self.state = 204
            self.match(compiladoresParser.ASIG)
            self.state = 205
            self.match(compiladoresParser.ID)
            self.state = 206
            self.iteracion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IteracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def SUMA(self):
            return self.getToken(compiladoresParser.SUMA, 0)

        def RESTA(self):
            return self.getToken(compiladoresParser.RESTA, 0)

        def MULT(self):
            return self.getToken(compiladoresParser.MULT, 0)

        def DIV(self):
            return self.getToken(compiladoresParser.DIV, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_iteracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIteracion" ):
                listener.enterIteracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIteracion" ):
                listener.exitIteracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIteracion" ):
                return visitor.visitIteracion(self)
            else:
                return visitor.visitChildren(self)




    def iteracion(self):

        localctx = compiladoresParser.IteracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_iteracion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62914560) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 209
            self.match(compiladoresParser.NUMERO)
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

        def cond(self):
            return self.getTypedRuleContext(compiladoresParser.CondContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.BloqueContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.BloqueContext,i)


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
        self.enterRule(localctx, 48, self.RULE_iif)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(compiladoresParser.IF)
            self.state = 212
            self.match(compiladoresParser.PA)
            self.state = 213
            self.cond()
            self.state = 214
            self.match(compiladoresParser.PC)
            self.state = 215
            self.bloque()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 216
                self.match(compiladoresParser.ELSE)
                self.state = 217
                self.bloque()


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
        self.enterRule(localctx, 50, self.RULE_returnfun)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(compiladoresParser.RETURN)
                self.state = 221
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
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
        self.enterRule(localctx, 52, self.RULE_ids)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 60129550336) != 0):
                self.state = 225
                self.exp()
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==18:
                    self.state = 226
                    self.match(compiladoresParser.COMA)
                    self.state = 227
                    self.exp()
                    self.state = 232
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
        self.enterRule(localctx, 54, self.RULE_funcionVar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(compiladoresParser.ID)
            self.state = 236
            self.match(compiladoresParser.PA)
            self.state = 237
            self.ids()
            self.state = 238
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
        self.enterRule(localctx, 56, self.RULE_llamadafun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.funcionVar()
            self.state = 241
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

        def term(self):
            return self.getTypedRuleContext(compiladoresParser.TermContext,0)


        def expPrima(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.ExpPrimaContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.ExpPrimaContext,i)


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




    def exp(self):

        localctx = compiladoresParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.term()
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==23:
                self.state = 244
                self.expPrima()
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpPrimaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(compiladoresParser.TermContext,0)


        def SUMA(self):
            return self.getToken(compiladoresParser.SUMA, 0)

        def RESTA(self):
            return self.getToken(compiladoresParser.RESTA, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_expPrima

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpPrima" ):
                listener.enterExpPrima(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpPrima" ):
                listener.exitExpPrima(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpPrima" ):
                return visitor.visitExpPrima(self)
            else:
                return visitor.visitChildren(self)




    def expPrima(self):

        localctx = compiladoresParser.ExpPrimaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expPrima)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 251
            self.term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def t(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.TContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.TContext,i)


        def getRuleIndex(self):
            return compiladoresParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = compiladoresParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.factor()
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0):
                self.state = 254
                self.t()
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def MULT(self):
            return self.getToken(compiladoresParser.MULT, 0)

        def DIV(self):
            return self.getToken(compiladoresParser.DIV, 0)

        def MOD(self):
            return self.getToken(compiladoresParser.MOD, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT" ):
                listener.enterT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT" ):
                listener.exitT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT" ):
                return visitor.visitT(self)
            else:
                return visitor.visitChildren(self)




    def t(self):

        localctx = compiladoresParser.TContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_t)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 261
            self.factor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 66, self.RULE_factor)
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(compiladoresParser.DECIMAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 265
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 266
                self.funcionVar()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 267
                self.match(compiladoresParser.PA)
                self.state = 268
                self.exp()
                self.state = 269
                self.match(compiladoresParser.PC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpcompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def MEN(self):
            return self.getToken(compiladoresParser.MEN, 0)

        def MAY(self):
            return self.getToken(compiladoresParser.MAY, 0)

        def MENI(self):
            return self.getToken(compiladoresParser.MENI, 0)

        def MAYI(self):
            return self.getToken(compiladoresParser.MAYI, 0)

        def IGUAL(self):
            return self.getToken(compiladoresParser.IGUAL, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_opcomp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpcomp" ):
                listener.enterOpcomp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpcomp" ):
                listener.exitOpcomp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcomp" ):
                return visitor.visitOpcomp(self)
            else:
                return visitor.visitChildren(self)




    def opcomp(self):

        localctx = compiladoresParser.OpcompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_opcomp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(compiladoresParser.ID)
            self.state = 274
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2015363072) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 275
            self.factor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpboolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.TRUE)
            else:
                return self.getToken(compiladoresParser.TRUE, i)

        def FALSE(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.FALSE)
            else:
                return self.getToken(compiladoresParser.FALSE, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.OR)
            else:
                return self.getToken(compiladoresParser.OR, i)

        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.AND)
            else:
                return self.getToken(compiladoresParser.AND, i)

        def getRuleIndex(self):
            return compiladoresParser.RULE_opbool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpbool" ):
                listener.enterOpbool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpbool" ):
                listener.exitOpbool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpbool" ):
                return visitor.visitOpbool(self)
            else:
                return visitor.visitChildren(self)




    def opbool(self):

        localctx = compiladoresParser.OpboolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_opbool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31 or _la==32:
                self.state = 278
                _la = self._input.LA(1)
                if not(_la==31 or _la==32):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 279
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opcomp(self):
            return self.getTypedRuleContext(compiladoresParser.OpcompContext,0)


        def opbool(self):
            return self.getTypedRuleContext(compiladoresParser.OpboolContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)




    def cond(self):

        localctx = compiladoresParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_cond)
        try:
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.opcomp()
                pass
            elif token in [11, 12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.opbool()
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





