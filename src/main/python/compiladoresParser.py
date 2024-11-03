# Generated from c:/Users/Usuario/OneDrive/Documentos/Facultad/iua/tercero/DHS/compilador/src/main/python/compiladores.g4 by ANTLR 4.13.1
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
        4,1,36,278,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,84,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,93,8,3,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,3,4,102,8,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,
        1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,121,8,9,1,10,1,10,3,10,125,
        8,10,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,3,13,
        138,8,13,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,3,15,156,8,15,1,16,1,16,1,17,1,17,1,17,
        1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,3,19,
        175,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,186,8,
        20,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,24,1,24,1,24,1,
        24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,
        27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,220,8,27,1,28,1,28,1,28,1,
        28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,235,8,29,1,
        30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,32,1,32,3,32,248,8,
        32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,3,
        33,262,8,33,1,34,1,34,1,34,1,34,3,34,268,8,34,1,35,1,35,1,35,3,35,
        273,8,35,1,36,1,36,1,36,1,36,0,0,37,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,
        66,68,70,72,0,3,1,0,24,27,2,0,23,23,34,34,2,0,21,22,34,34,270,0,
        74,1,0,0,0,2,83,1,0,0,0,4,85,1,0,0,0,6,92,1,0,0,0,8,101,1,0,0,0,
        10,103,1,0,0,0,12,106,1,0,0,0,14,109,1,0,0,0,16,111,1,0,0,0,18,120,
        1,0,0,0,20,124,1,0,0,0,22,126,1,0,0,0,24,129,1,0,0,0,26,137,1,0,
        0,0,28,139,1,0,0,0,30,155,1,0,0,0,32,157,1,0,0,0,34,159,1,0,0,0,
        36,165,1,0,0,0,38,174,1,0,0,0,40,185,1,0,0,0,42,187,1,0,0,0,44,189,
        1,0,0,0,46,193,1,0,0,0,48,196,1,0,0,0,50,200,1,0,0,0,52,210,1,0,
        0,0,54,219,1,0,0,0,56,221,1,0,0,0,58,234,1,0,0,0,60,236,1,0,0,0,
        62,242,1,0,0,0,64,247,1,0,0,0,66,261,1,0,0,0,68,267,1,0,0,0,70,272,
        1,0,0,0,72,274,1,0,0,0,74,75,3,2,1,0,75,76,5,0,0,1,76,1,1,0,0,0,
        77,78,5,1,0,0,78,79,3,2,1,0,79,80,5,2,0,0,80,81,3,2,1,0,81,84,1,
        0,0,0,82,84,1,0,0,0,83,77,1,0,0,0,83,82,1,0,0,0,84,3,1,0,0,0,85,
        86,3,6,3,0,86,87,5,0,0,1,87,5,1,0,0,0,88,89,3,8,4,0,89,90,3,6,3,
        0,90,93,1,0,0,0,91,93,1,0,0,0,92,88,1,0,0,0,92,91,1,0,0,0,93,7,1,
        0,0,0,94,102,3,16,8,0,95,102,3,34,17,0,96,102,3,50,25,0,97,102,3,
        60,30,0,98,102,3,36,18,0,99,102,3,22,11,0,100,102,3,66,33,0,101,
        94,1,0,0,0,101,95,1,0,0,0,101,96,1,0,0,0,101,97,1,0,0,0,101,98,1,
        0,0,0,101,99,1,0,0,0,101,100,1,0,0,0,102,9,1,0,0,0,103,104,3,14,
        7,0,104,105,3,20,10,0,105,11,1,0,0,0,106,107,3,14,7,0,107,108,5,
        34,0,0,108,13,1,0,0,0,109,110,7,0,0,0,110,15,1,0,0,0,111,112,3,12,
        6,0,112,113,5,3,0,0,113,17,1,0,0,0,114,115,5,34,0,0,115,116,5,8,
        0,0,116,121,3,24,12,0,117,118,5,34,0,0,118,119,5,8,0,0,119,121,5,
        23,0,0,120,114,1,0,0,0,120,117,1,0,0,0,121,19,1,0,0,0,122,125,3,
        18,9,0,123,125,3,44,22,0,124,122,1,0,0,0,124,123,1,0,0,0,125,21,
        1,0,0,0,126,127,3,20,10,0,127,128,5,3,0,0,128,23,1,0,0,0,129,130,
        3,28,14,0,130,131,3,26,13,0,131,25,1,0,0,0,132,133,5,10,0,0,133,
        138,3,24,12,0,134,135,5,11,0,0,135,138,3,24,12,0,136,138,1,0,0,0,
        137,132,1,0,0,0,137,134,1,0,0,0,137,136,1,0,0,0,138,27,1,0,0,0,139,
        140,3,32,16,0,140,141,3,30,15,0,141,29,1,0,0,0,142,143,5,12,0,0,
        143,144,3,32,16,0,144,145,3,30,15,0,145,156,1,0,0,0,146,147,5,13,
        0,0,147,148,3,32,16,0,148,149,3,30,15,0,149,156,1,0,0,0,150,151,
        5,14,0,0,151,152,3,32,16,0,152,153,3,30,15,0,153,156,1,0,0,0,154,
        156,1,0,0,0,155,142,1,0,0,0,155,146,1,0,0,0,155,150,1,0,0,0,155,
        154,1,0,0,0,156,31,1,0,0,0,157,158,7,1,0,0,158,33,1,0,0,0,159,160,
        5,29,0,0,160,161,5,1,0,0,161,162,5,34,0,0,162,163,5,2,0,0,163,164,
        3,8,4,0,164,35,1,0,0,0,165,166,5,4,0,0,166,167,3,6,3,0,167,168,5,
        5,0,0,168,37,1,0,0,0,169,175,5,16,0,0,170,175,5,15,0,0,171,175,5,
        18,0,0,172,175,5,17,0,0,173,175,1,0,0,0,174,169,1,0,0,0,174,170,
        1,0,0,0,174,171,1,0,0,0,174,172,1,0,0,0,174,173,1,0,0,0,175,39,1,
        0,0,0,176,177,5,19,0,0,177,178,3,42,21,0,178,179,3,40,20,0,179,186,
        1,0,0,0,180,181,5,20,0,0,181,182,3,42,21,0,182,183,3,40,20,0,183,
        186,1,0,0,0,184,186,1,0,0,0,185,176,1,0,0,0,185,180,1,0,0,0,185,
        184,1,0,0,0,186,41,1,0,0,0,187,188,7,2,0,0,188,43,1,0,0,0,189,190,
        5,34,0,0,190,191,5,8,0,0,191,192,3,46,23,0,192,45,1,0,0,0,193,194,
        3,42,21,0,194,195,3,40,20,0,195,47,1,0,0,0,196,197,5,34,0,0,197,
        198,3,38,19,0,198,199,3,32,16,0,199,49,1,0,0,0,200,201,5,30,0,0,
        201,202,5,1,0,0,202,203,3,52,26,0,203,204,5,3,0,0,204,205,3,54,27,
        0,205,206,5,3,0,0,206,207,3,56,28,0,207,208,5,2,0,0,208,209,3,36,
        18,0,209,51,1,0,0,0,210,211,3,18,9,0,211,53,1,0,0,0,212,213,3,48,
        24,0,213,214,3,54,27,0,214,220,1,0,0,0,215,216,3,46,23,0,216,217,
        3,54,27,0,217,220,1,0,0,0,218,220,1,0,0,0,219,212,1,0,0,0,219,215,
        1,0,0,0,219,218,1,0,0,0,220,55,1,0,0,0,221,222,5,34,0,0,222,223,
        5,8,0,0,223,224,5,34,0,0,224,225,3,58,29,0,225,57,1,0,0,0,226,227,
        5,10,0,0,227,235,5,23,0,0,228,229,5,11,0,0,229,235,5,23,0,0,230,
        231,5,12,0,0,231,235,5,23,0,0,232,233,5,13,0,0,233,235,5,23,0,0,
        234,226,1,0,0,0,234,228,1,0,0,0,234,230,1,0,0,0,234,232,1,0,0,0,
        235,59,1,0,0,0,236,237,5,31,0,0,237,238,5,1,0,0,238,239,3,54,27,
        0,239,240,5,2,0,0,240,241,3,36,18,0,241,61,1,0,0,0,242,243,5,32,
        0,0,243,244,3,64,32,0,244,63,1,0,0,0,245,248,3,60,30,0,246,248,3,
        36,18,0,247,245,1,0,0,0,247,246,1,0,0,0,248,65,1,0,0,0,249,250,3,
        14,7,0,250,251,5,34,0,0,251,252,5,1,0,0,252,253,3,68,34,0,253,254,
        5,2,0,0,254,262,1,0,0,0,255,256,5,28,0,0,256,257,5,34,0,0,257,258,
        5,1,0,0,258,259,3,68,34,0,259,260,5,2,0,0,260,262,1,0,0,0,261,249,
        1,0,0,0,261,255,1,0,0,0,262,67,1,0,0,0,263,264,3,72,36,0,264,265,
        3,70,35,0,265,268,1,0,0,0,266,268,1,0,0,0,267,263,1,0,0,0,267,266,
        1,0,0,0,268,69,1,0,0,0,269,270,5,6,0,0,270,273,3,68,34,0,271,273,
        1,0,0,0,272,269,1,0,0,0,272,271,1,0,0,0,273,71,1,0,0,0,274,275,3,
        14,7,0,275,276,5,34,0,0,276,73,1,0,0,0,15,83,92,101,120,124,137,
        155,174,185,219,234,247,261,267,272
    ]

class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "';'", "'{'", "'}'", "','", 
                     "'.'", "'='", "'=='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'>'", "'<'", "'>='", "'<='", "'||'", "'&&'", "'true'", 
                     "'false'", "<INVALID>", "'int'", "'bool'", "'float'", 
                     "'double'", "'void'", "'while'", "'for'", "'if'", "'else'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "PYC", "LLA", "LLC", "COMA", 
                      "PUNTO", "ASIG", "IGUAL", "SUMA", "RESTA", "MULT", 
                      "DIV", "MOD", "MAY", "MEN", "MAYI", "MENI", "OR", 
                      "AND", "TRUE", "FALSE", "NUMERO", "INT", "BOOL", "FLOAT", 
                      "DOUBLE", "VOID", "WHILE", "FOR", "IF", "ELSE", "BOOLEANS", 
                      "ID", "WS", "OTRO" ]

    RULE_si = 0
    RULE_s = 1
    RULE_programa = 2
    RULE_instrucciones = 3
    RULE_instruccion = 4
    RULE_inic = 5
    RULE_declaracion = 6
    RULE_tipoDatos = 7
    RULE_declaracionPYC = 8
    RULE_asignacionNum = 9
    RULE_asignacion = 10
    RULE_inst = 11
    RULE_exp = 12
    RULE_expPrima = 13
    RULE_term = 14
    RULE_t = 15
    RULE_factor = 16
    RULE_iwhile = 17
    RULE_bloque = 18
    RULE_comps = 19
    RULE_bools = 20
    RULE_factorBool = 21
    RULE_asignacionBool = 22
    RULE_opbool = 23
    RULE_opcomp = 24
    RULE_ifor = 25
    RULE_init = 26
    RULE_cond = 27
    RULE_iter = 28
    RULE_iteracion = 29
    RULE_iif = 30
    RULE_else = 31
    RULE_eelse = 32
    RULE_funciones = 33
    RULE_argumentos = 34
    RULE_arg = 35
    RULE_argumento = 36

    ruleNames =  [ "si", "s", "programa", "instrucciones", "instruccion", 
                   "inic", "declaracion", "tipoDatos", "declaracionPYC", 
                   "asignacionNum", "asignacion", "inst", "exp", "expPrima", 
                   "term", "t", "factor", "iwhile", "bloque", "comps", "bools", 
                   "factorBool", "asignacionBool", "opbool", "opcomp", "ifor", 
                   "init", "cond", "iter", "iteracion", "iif", "else", "eelse", 
                   "funciones", "argumentos", "arg", "argumento" ]

    EOF = Token.EOF
    PA=1
    PC=2
    PYC=3
    LLA=4
    LLC=5
    COMA=6
    PUNTO=7
    ASIG=8
    IGUAL=9
    SUMA=10
    RESTA=11
    MULT=12
    DIV=13
    MOD=14
    MAY=15
    MEN=16
    MAYI=17
    MENI=18
    OR=19
    AND=20
    TRUE=21
    FALSE=22
    NUMERO=23
    INT=24
    BOOL=25
    FLOAT=26
    DOUBLE=27
    VOID=28
    WHILE=29
    FOR=30
    IF=31
    ELSE=32
    BOOLEANS=33
    ID=34
    WS=35
    OTRO=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s(self):
            return self.getTypedRuleContext(compiladoresParser.SContext,0)


        def EOF(self):
            return self.getToken(compiladoresParser.EOF, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_si

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSi" ):
                listener.enterSi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSi" ):
                listener.exitSi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSi" ):
                return visitor.visitSi(self)
            else:
                return visitor.visitChildren(self)




    def si(self):

        localctx = compiladoresParser.SiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_si)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.s()
            self.state = 75
            self.match(compiladoresParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def s(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.SContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.SContext,i)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS" ):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = compiladoresParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_s)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(compiladoresParser.PA)
                self.state = 78
                self.s()
                self.state = 79
                self.match(compiladoresParser.PC)
                self.state = 80
                self.s()
                pass
            elif token in [-1, 2]:
                self.enterOuterAlt(localctx, 2)

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
        self.enterRule(localctx, 4, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.instrucciones()
            self.state = 86
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

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


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
        self.enterRule(localctx, 6, self.RULE_instrucciones)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 24, 25, 26, 27, 28, 29, 30, 31, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.instruccion()
                self.state = 89
                self.instrucciones()
                pass
            elif token in [-1, 5]:
                self.enterOuterAlt(localctx, 2)

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


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionPYC(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionPYCContext,0)


        def iwhile(self):
            return self.getTypedRuleContext(compiladoresParser.IwhileContext,0)


        def ifor(self):
            return self.getTypedRuleContext(compiladoresParser.IforContext,0)


        def iif(self):
            return self.getTypedRuleContext(compiladoresParser.IifContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def inst(self):
            return self.getTypedRuleContext(compiladoresParser.InstContext,0)


        def funciones(self):
            return self.getTypedRuleContext(compiladoresParser.FuncionesContext,0)


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
        self.enterRule(localctx, 8, self.RULE_instruccion)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.declaracionPYC()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.iwhile()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.ifor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self.iif()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 98
                self.bloque()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 99
                self.inst()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 100
                self.funciones()
                pass


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


        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


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
        self.enterRule(localctx, 10, self.RULE_inic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.tipoDatos()
            self.state = 104
            self.asignacion()
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


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

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
        self.enterRule(localctx, 12, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.tipoDatos()
            self.state = 107
            self.match(compiladoresParser.ID)
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
            self.state = 109
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 251658240) != 0)):
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
        self.enterRule(localctx, 16, self.RULE_declaracionPYC)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.declaracion()
            self.state = 112
            self.match(compiladoresParser.PYC)
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


        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

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
        self.enterRule(localctx, 18, self.RULE_asignacionNum)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.match(compiladoresParser.ID)
                self.state = 115
                self.match(compiladoresParser.ASIG)
                self.state = 116
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(compiladoresParser.ID)
                self.state = 118
                self.match(compiladoresParser.ASIG)
                self.state = 119
                self.match(compiladoresParser.NUMERO)
                pass


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
        self.enterRule(localctx, 20, self.RULE_asignacion)
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.asignacionNum()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.asignacionBool()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_inst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInst" ):
                listener.enterInst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInst" ):
                listener.exitInst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInst" ):
                return visitor.visitInst(self)
            else:
                return visitor.visitChildren(self)




    def inst(self):

        localctx = compiladoresParser.InstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_inst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.asignacion()
            self.state = 127
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


        def expPrima(self):
            return self.getTypedRuleContext(compiladoresParser.ExpPrimaContext,0)


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
        self.enterRule(localctx, 24, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.term()
            self.state = 130
            self.expPrima()
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

        def SUMA(self):
            return self.getToken(compiladoresParser.SUMA, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


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
        self.enterRule(localctx, 26, self.RULE_expPrima)
        try:
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(compiladoresParser.SUMA)
                self.state = 133
                self.exp()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(compiladoresParser.RESTA)
                self.state = 135
                self.exp()
                pass
            elif token in [-1, 3]:
                self.enterOuterAlt(localctx, 3)

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


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladoresParser.TContext,0)


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
        self.enterRule(localctx, 28, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.factor()
            self.state = 140
            self.t()
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

        def MULT(self):
            return self.getToken(compiladoresParser.MULT, 0)

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladoresParser.TContext,0)


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
        self.enterRule(localctx, 30, self.RULE_t)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(compiladoresParser.MULT)
                self.state = 143
                self.factor()
                self.state = 144
                self.t()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.match(compiladoresParser.DIV)
                self.state = 147
                self.factor()
                self.state = 148
                self.t()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.match(compiladoresParser.MOD)
                self.state = 151
                self.factor()
                self.state = 152
                self.t()
                pass
            elif token in [-1, 3, 10, 11]:
                self.enterOuterAlt(localctx, 4)

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


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

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
        self.enterRule(localctx, 32, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            _la = self._input.LA(1)
            if not(_la==23 or _la==34):
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


    class IwhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(compiladoresParser.WHILE, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


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
        self.enterRule(localctx, 34, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(compiladoresParser.WHILE)
            self.state = 160
            self.match(compiladoresParser.PA)
            self.state = 161
            self.match(compiladoresParser.ID)
            self.state = 162
            self.match(compiladoresParser.PC)
            self.state = 163
            self.instruccion()
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
        self.enterRule(localctx, 36, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(compiladoresParser.LLA)
            self.state = 166
            self.instrucciones()
            self.state = 167
            self.match(compiladoresParser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MEN(self):
            return self.getToken(compiladoresParser.MEN, 0)

        def MAY(self):
            return self.getToken(compiladoresParser.MAY, 0)

        def MENI(self):
            return self.getToken(compiladoresParser.MENI, 0)

        def MAYI(self):
            return self.getToken(compiladoresParser.MAYI, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_comps

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComps" ):
                listener.enterComps(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComps" ):
                listener.exitComps(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComps" ):
                return visitor.visitComps(self)
            else:
                return visitor.visitChildren(self)




    def comps(self):

        localctx = compiladoresParser.CompsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_comps)
        try:
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(compiladoresParser.MEN)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.match(compiladoresParser.MAY)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 171
                self.match(compiladoresParser.MENI)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 172
                self.match(compiladoresParser.MAYI)
                pass
            elif token in [23, 34]:
                self.enterOuterAlt(localctx, 5)

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


    class BoolsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(compiladoresParser.OR, 0)

        def factorBool(self):
            return self.getTypedRuleContext(compiladoresParser.FactorBoolContext,0)


        def bools(self):
            return self.getTypedRuleContext(compiladoresParser.BoolsContext,0)


        def AND(self):
            return self.getToken(compiladoresParser.AND, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_bools

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBools" ):
                listener.enterBools(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBools" ):
                listener.exitBools(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBools" ):
                return visitor.visitBools(self)
            else:
                return visitor.visitChildren(self)




    def bools(self):

        localctx = compiladoresParser.BoolsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_bools)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(compiladoresParser.OR)
                self.state = 177
                self.factorBool()
                self.state = 178
                self.bools()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.match(compiladoresParser.AND)
                self.state = 181
                self.factorBool()
                self.state = 182
                self.bools()
                pass
            elif token in [-1, 2, 3, 21, 22, 34]:
                self.enterOuterAlt(localctx, 3)

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


    class FactorBoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def TRUE(self):
            return self.getToken(compiladoresParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(compiladoresParser.FALSE, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_factorBool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorBool" ):
                listener.enterFactorBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorBool" ):
                listener.exitFactorBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactorBool" ):
                return visitor.visitFactorBool(self)
            else:
                return visitor.visitChildren(self)




    def factorBool(self):

        localctx = compiladoresParser.FactorBoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_factorBool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17186160640) != 0)):
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
        self.enterRule(localctx, 44, self.RULE_asignacionBool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(compiladoresParser.ID)
            self.state = 190
            self.match(compiladoresParser.ASIG)
            self.state = 191
            self.opbool()
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

        def factorBool(self):
            return self.getTypedRuleContext(compiladoresParser.FactorBoolContext,0)


        def bools(self):
            return self.getTypedRuleContext(compiladoresParser.BoolsContext,0)


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
        self.enterRule(localctx, 46, self.RULE_opbool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.factorBool()
            self.state = 194
            self.bools()
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

        def comps(self):
            return self.getTypedRuleContext(compiladoresParser.CompsContext,0)


        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


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
        self.enterRule(localctx, 48, self.RULE_opcomp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(compiladoresParser.ID)
            self.state = 197
            self.comps()
            self.state = 198
            self.factor()
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
        self.enterRule(localctx, 50, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(compiladoresParser.FOR)
            self.state = 201
            self.match(compiladoresParser.PA)
            self.state = 202
            self.init()
            self.state = 203
            self.match(compiladoresParser.PYC)
            self.state = 204
            self.cond()
            self.state = 205
            self.match(compiladoresParser.PYC)
            self.state = 206
            self.iter_()
            self.state = 207
            self.match(compiladoresParser.PC)
            self.state = 208
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
        self.enterRule(localctx, 52, self.RULE_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.asignacionNum()
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


        def cond(self):
            return self.getTypedRuleContext(compiladoresParser.CondContext,0)


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
        self.enterRule(localctx, 54, self.RULE_cond)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.opcomp()
                self.state = 213
                self.cond()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.opbool()
                self.state = 216
                self.cond()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


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
        self.enterRule(localctx, 56, self.RULE_iter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(compiladoresParser.ID)
            self.state = 222
            self.match(compiladoresParser.ASIG)
            self.state = 223
            self.match(compiladoresParser.ID)
            self.state = 224
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

        def SUMA(self):
            return self.getToken(compiladoresParser.SUMA, 0)

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

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
        self.enterRule(localctx, 58, self.RULE_iteracion)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(compiladoresParser.SUMA)
                self.state = 227
                self.match(compiladoresParser.NUMERO)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.match(compiladoresParser.RESTA)
                self.state = 229
                self.match(compiladoresParser.NUMERO)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.match(compiladoresParser.MULT)
                self.state = 231
                self.match(compiladoresParser.NUMERO)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 232
                self.match(compiladoresParser.DIV)
                self.state = 233
                self.match(compiladoresParser.NUMERO)
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

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


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
        self.enterRule(localctx, 60, self.RULE_iif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(compiladoresParser.IF)
            self.state = 237
            self.match(compiladoresParser.PA)
            self.state = 238
            self.cond()
            self.state = 239
            self.match(compiladoresParser.PC)
            self.state = 240
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(compiladoresParser.ELSE, 0)

        def eelse(self):
            return self.getTypedRuleContext(compiladoresParser.EelseContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse" ):
                listener.enterElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse" ):
                listener.exitElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse" ):
                return visitor.visitElse(self)
            else:
                return visitor.visitChildren(self)




    def else_(self):

        localctx = compiladoresParser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(compiladoresParser.ELSE)
            self.state = 243
            self.eelse()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EelseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iif(self):
            return self.getTypedRuleContext(compiladoresParser.IifContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_eelse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEelse" ):
                listener.enterEelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEelse" ):
                listener.exitEelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEelse" ):
                return visitor.visitEelse(self)
            else:
                return visitor.visitChildren(self)




    def eelse(self):

        localctx = compiladoresParser.EelseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_eelse)
        try:
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.iif()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.bloque()
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


    class FuncionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipoDatos(self):
            return self.getTypedRuleContext(compiladoresParser.TipoDatosContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def argumentos(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentosContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def VOID(self):
            return self.getToken(compiladoresParser.VOID, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_funciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunciones" ):
                listener.enterFunciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunciones" ):
                listener.exitFunciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunciones" ):
                return visitor.visitFunciones(self)
            else:
                return visitor.visitChildren(self)




    def funciones(self):

        localctx = compiladoresParser.FuncionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_funciones)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 25, 26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.tipoDatos()
                self.state = 250
                self.match(compiladoresParser.ID)
                self.state = 251
                self.match(compiladoresParser.PA)
                self.state = 252
                self.argumentos()
                self.state = 253
                self.match(compiladoresParser.PC)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(compiladoresParser.VOID)
                self.state = 256
                self.match(compiladoresParser.ID)
                self.state = 257
                self.match(compiladoresParser.PA)
                self.state = 258
                self.argumentos()
                self.state = 259
                self.match(compiladoresParser.PC)
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


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argumento(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentoContext,0)


        def arg(self):
            return self.getTypedRuleContext(compiladoresParser.ArgContext,0)


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
        self.enterRule(localctx, 68, self.RULE_argumentos)
        try:
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 25, 26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.argumento()
                self.state = 264
                self.arg()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)

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


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladoresParser.COMA, 0)

        def argumentos(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg" ):
                listener.enterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg" ):
                listener.exitArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = compiladoresParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_arg)
        try:
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(compiladoresParser.COMA)
                self.state = 270
                self.argumentos()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)

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
        self.enterRule(localctx, 72, self.RULE_argumento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.tipoDatos()
            self.state = 275
            self.match(compiladoresParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





