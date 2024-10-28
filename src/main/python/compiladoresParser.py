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
        4,1,36,287,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,3,1,86,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,95,8,
        3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,103,8,4,1,5,1,5,1,5,1,6,1,6,1,6,1,
        7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,122,8,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,133,8,10,1,11,1,11,1,11,
        1,12,1,12,3,12,140,8,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,
        3,14,150,8,14,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,3,16,168,8,16,1,17,1,17,1,18,1,18,
        1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,
        3,20,187,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,
        198,8,21,1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,25,1,25,
        1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,
        1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,232,8,28,1,29,1,29,
        1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,247,
        8,30,1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,33,1,33,3,33,
        260,8,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,
        1,34,3,34,274,8,34,1,35,1,35,1,35,1,36,1,36,1,36,3,36,282,8,36,1,
        37,1,37,1,37,1,37,0,0,38,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,
        74,0,3,1,0,24,27,2,0,23,23,34,34,2,0,21,22,34,34,278,0,76,1,0,0,
        0,2,85,1,0,0,0,4,87,1,0,0,0,6,94,1,0,0,0,8,102,1,0,0,0,10,104,1,
        0,0,0,12,107,1,0,0,0,14,110,1,0,0,0,16,112,1,0,0,0,18,121,1,0,0,
        0,20,132,1,0,0,0,22,134,1,0,0,0,24,139,1,0,0,0,26,141,1,0,0,0,28,
        149,1,0,0,0,30,151,1,0,0,0,32,167,1,0,0,0,34,169,1,0,0,0,36,171,
        1,0,0,0,38,177,1,0,0,0,40,186,1,0,0,0,42,197,1,0,0,0,44,199,1,0,
        0,0,46,201,1,0,0,0,48,205,1,0,0,0,50,208,1,0,0,0,52,212,1,0,0,0,
        54,222,1,0,0,0,56,231,1,0,0,0,58,233,1,0,0,0,60,246,1,0,0,0,62,248,
        1,0,0,0,64,254,1,0,0,0,66,259,1,0,0,0,68,273,1,0,0,0,70,275,1,0,
        0,0,72,281,1,0,0,0,74,283,1,0,0,0,76,77,3,2,1,0,77,78,5,0,0,1,78,
        1,1,0,0,0,79,80,5,1,0,0,80,81,3,2,1,0,81,82,5,2,0,0,82,83,3,2,1,
        0,83,86,1,0,0,0,84,86,1,0,0,0,85,79,1,0,0,0,85,84,1,0,0,0,86,3,1,
        0,0,0,87,88,3,6,3,0,88,89,5,0,0,1,89,5,1,0,0,0,90,91,3,8,4,0,91,
        92,3,6,3,0,92,95,1,0,0,0,93,95,1,0,0,0,94,90,1,0,0,0,94,93,1,0,0,
        0,95,7,1,0,0,0,96,103,3,16,8,0,97,103,3,36,18,0,98,103,3,52,26,0,
        99,103,3,62,31,0,100,103,3,38,19,0,101,103,3,22,11,0,102,96,1,0,
        0,0,102,97,1,0,0,0,102,98,1,0,0,0,102,99,1,0,0,0,102,100,1,0,0,0,
        102,101,1,0,0,0,103,9,1,0,0,0,104,105,3,14,7,0,105,106,3,20,10,0,
        106,11,1,0,0,0,107,108,3,14,7,0,108,109,5,34,0,0,109,13,1,0,0,0,
        110,111,7,0,0,0,111,15,1,0,0,0,112,113,3,12,6,0,113,114,5,3,0,0,
        114,17,1,0,0,0,115,116,5,34,0,0,116,117,5,8,0,0,117,122,3,26,13,
        0,118,119,5,34,0,0,119,120,5,8,0,0,120,122,5,23,0,0,121,115,1,0,
        0,0,121,118,1,0,0,0,122,19,1,0,0,0,123,124,5,34,0,0,124,125,5,8,
        0,0,125,133,3,24,12,0,126,127,5,34,0,0,127,128,5,8,0,0,128,133,5,
        23,0,0,129,130,5,34,0,0,130,131,5,8,0,0,131,133,5,33,0,0,132,123,
        1,0,0,0,132,126,1,0,0,0,132,129,1,0,0,0,133,21,1,0,0,0,134,135,3,
        20,10,0,135,136,5,3,0,0,136,23,1,0,0,0,137,140,3,26,13,0,138,140,
        3,48,24,0,139,137,1,0,0,0,139,138,1,0,0,0,140,25,1,0,0,0,141,142,
        3,30,15,0,142,143,3,28,14,0,143,27,1,0,0,0,144,145,5,10,0,0,145,
        150,3,26,13,0,146,147,5,11,0,0,147,150,3,26,13,0,148,150,1,0,0,0,
        149,144,1,0,0,0,149,146,1,0,0,0,149,148,1,0,0,0,150,29,1,0,0,0,151,
        152,3,34,17,0,152,153,3,32,16,0,153,31,1,0,0,0,154,155,5,12,0,0,
        155,156,3,34,17,0,156,157,3,32,16,0,157,168,1,0,0,0,158,159,5,13,
        0,0,159,160,3,34,17,0,160,161,3,32,16,0,161,168,1,0,0,0,162,163,
        5,14,0,0,163,164,3,34,17,0,164,165,3,32,16,0,165,168,1,0,0,0,166,
        168,1,0,0,0,167,154,1,0,0,0,167,158,1,0,0,0,167,162,1,0,0,0,167,
        166,1,0,0,0,168,33,1,0,0,0,169,170,7,1,0,0,170,35,1,0,0,0,171,172,
        5,29,0,0,172,173,5,1,0,0,173,174,5,34,0,0,174,175,5,2,0,0,175,176,
        3,8,4,0,176,37,1,0,0,0,177,178,5,4,0,0,178,179,3,6,3,0,179,180,5,
        5,0,0,180,39,1,0,0,0,181,187,5,16,0,0,182,187,5,15,0,0,183,187,5,
        18,0,0,184,187,5,17,0,0,185,187,1,0,0,0,186,181,1,0,0,0,186,182,
        1,0,0,0,186,183,1,0,0,0,186,184,1,0,0,0,186,185,1,0,0,0,187,41,1,
        0,0,0,188,189,5,19,0,0,189,190,3,44,22,0,190,191,3,42,21,0,191,198,
        1,0,0,0,192,193,5,20,0,0,193,194,3,44,22,0,194,195,3,42,21,0,195,
        198,1,0,0,0,196,198,1,0,0,0,197,188,1,0,0,0,197,192,1,0,0,0,197,
        196,1,0,0,0,198,43,1,0,0,0,199,200,7,2,0,0,200,45,1,0,0,0,201,202,
        5,34,0,0,202,203,5,8,0,0,203,204,3,48,24,0,204,47,1,0,0,0,205,206,
        3,44,22,0,206,207,3,42,21,0,207,49,1,0,0,0,208,209,5,34,0,0,209,
        210,3,40,20,0,210,211,3,34,17,0,211,51,1,0,0,0,212,213,5,30,0,0,
        213,214,5,1,0,0,214,215,3,54,27,0,215,216,5,3,0,0,216,217,3,56,28,
        0,217,218,5,3,0,0,218,219,3,58,29,0,219,220,5,2,0,0,220,221,3,38,
        19,0,221,53,1,0,0,0,222,223,3,18,9,0,223,55,1,0,0,0,224,225,3,50,
        25,0,225,226,3,56,28,0,226,232,1,0,0,0,227,228,3,48,24,0,228,229,
        3,56,28,0,229,232,1,0,0,0,230,232,1,0,0,0,231,224,1,0,0,0,231,227,
        1,0,0,0,231,230,1,0,0,0,232,57,1,0,0,0,233,234,5,34,0,0,234,235,
        5,8,0,0,235,236,5,34,0,0,236,237,3,60,30,0,237,59,1,0,0,0,238,239,
        5,10,0,0,239,247,5,23,0,0,240,241,5,11,0,0,241,247,5,23,0,0,242,
        243,5,12,0,0,243,247,5,23,0,0,244,245,5,13,0,0,245,247,5,23,0,0,
        246,238,1,0,0,0,246,240,1,0,0,0,246,242,1,0,0,0,246,244,1,0,0,0,
        247,61,1,0,0,0,248,249,5,31,0,0,249,250,5,1,0,0,250,251,3,56,28,
        0,251,252,5,2,0,0,252,253,3,38,19,0,253,63,1,0,0,0,254,255,5,32,
        0,0,255,256,3,66,33,0,256,65,1,0,0,0,257,260,3,62,31,0,258,260,3,
        38,19,0,259,257,1,0,0,0,259,258,1,0,0,0,260,67,1,0,0,0,261,262,3,
        14,7,0,262,263,5,34,0,0,263,264,5,1,0,0,264,265,3,70,35,0,265,266,
        5,2,0,0,266,274,1,0,0,0,267,268,5,28,0,0,268,269,5,34,0,0,269,270,
        5,1,0,0,270,271,3,70,35,0,271,272,5,2,0,0,272,274,1,0,0,0,273,261,
        1,0,0,0,273,267,1,0,0,0,274,69,1,0,0,0,275,276,3,74,37,0,276,277,
        3,72,36,0,277,71,1,0,0,0,278,279,5,6,0,0,279,282,3,70,35,0,280,282,
        1,0,0,0,281,278,1,0,0,0,281,280,1,0,0,0,282,73,1,0,0,0,283,284,3,
        14,7,0,284,285,5,34,0,0,285,75,1,0,0,0,15,85,94,102,121,132,139,
        149,167,186,197,231,246,259,273,281
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
    RULE_opal = 12
    RULE_exp = 13
    RULE_expPrima = 14
    RULE_term = 15
    RULE_t = 16
    RULE_factor = 17
    RULE_iwhile = 18
    RULE_bloque = 19
    RULE_comps = 20
    RULE_bools = 21
    RULE_factorBool = 22
    RULE_asignacionBool = 23
    RULE_opbool = 24
    RULE_opcomp = 25
    RULE_ifor = 26
    RULE_init = 27
    RULE_cond = 28
    RULE_iter = 29
    RULE_iteracion = 30
    RULE_iif = 31
    RULE_else = 32
    RULE_eelse = 33
    RULE_funciones = 34
    RULE_argumentos = 35
    RULE_arg = 36
    RULE_argumento = 37

    ruleNames =  [ "si", "s", "programa", "instrucciones", "instruccion", 
                   "inic", "declaracion", "tipoDatos", "declaracionPYC", 
                   "asignacionNum", "asignacion", "inst", "opal", "exp", 
                   "expPrima", "term", "t", "factor", "iwhile", "bloque", 
                   "comps", "bools", "factorBool", "asignacionBool", "opbool", 
                   "opcomp", "ifor", "init", "cond", "iter", "iteracion", 
                   "iif", "else", "eelse", "funciones", "argumentos", "arg", 
                   "argumento" ]

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
            self.state = 76
            self.s()
            self.state = 77
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
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(compiladoresParser.PA)
                self.state = 80
                self.s()
                self.state = 81
                self.match(compiladoresParser.PC)
                self.state = 82
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
            self.state = 87
            self.instrucciones()
            self.state = 88
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
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 24, 25, 26, 27, 29, 30, 31, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.instruccion()
                self.state = 91
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
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 25, 26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.declaracionPYC()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.iwhile()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 98
                self.ifor()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 99
                self.iif()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 100
                self.bloque()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 6)
                self.state = 101
                self.inst()
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
            self.state = 104
            self.tipoDatos()
            self.state = 105
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
            self.state = 107
            self.tipoDatos()
            self.state = 108
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
            self.state = 110
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
            self.state = 112
            self.declaracion()
            self.state = 113
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
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(compiladoresParser.ID)
                self.state = 116
                self.match(compiladoresParser.ASIG)
                self.state = 117
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(compiladoresParser.ID)
                self.state = 119
                self.match(compiladoresParser.ASIG)
                self.state = 120
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

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def BOOLEANS(self):
            return self.getToken(compiladoresParser.BOOLEANS, 0)

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
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(compiladoresParser.ID)
                self.state = 124
                self.match(compiladoresParser.ASIG)
                self.state = 125
                self.opal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.match(compiladoresParser.ID)
                self.state = 127
                self.match(compiladoresParser.ASIG)
                self.state = 128
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.match(compiladoresParser.ID)
                self.state = 130
                self.match(compiladoresParser.ASIG)
                self.state = 131
                self.match(compiladoresParser.BOOLEANS)
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
            self.state = 134
            self.asignacion()
            self.state = 135
            self.match(compiladoresParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def opbool(self):
            return self.getTypedRuleContext(compiladoresParser.OpboolContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_opal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpal" ):
                listener.enterOpal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpal" ):
                listener.exitOpal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpal" ):
                return visitor.visitOpal(self)
            else:
                return visitor.visitChildren(self)




    def opal(self):

        localctx = compiladoresParser.OpalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_opal)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.opbool()
                pass


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
        self.enterRule(localctx, 26, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.term()
            self.state = 142
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
        self.enterRule(localctx, 28, self.RULE_expPrima)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(compiladoresParser.SUMA)
                self.state = 145
                self.exp()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.match(compiladoresParser.RESTA)
                self.state = 147
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
        self.enterRule(localctx, 30, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.factor()
            self.state = 152
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
        self.enterRule(localctx, 32, self.RULE_t)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(compiladoresParser.MULT)
                self.state = 155
                self.factor()
                self.state = 156
                self.t()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(compiladoresParser.DIV)
                self.state = 159
                self.factor()
                self.state = 160
                self.t()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 162
                self.match(compiladoresParser.MOD)
                self.state = 163
                self.factor()
                self.state = 164
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
        self.enterRule(localctx, 34, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
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
        self.enterRule(localctx, 36, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(compiladoresParser.WHILE)
            self.state = 172
            self.match(compiladoresParser.PA)
            self.state = 173
            self.match(compiladoresParser.ID)
            self.state = 174
            self.match(compiladoresParser.PC)
            self.state = 175
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
        self.enterRule(localctx, 38, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(compiladoresParser.LLA)
            self.state = 178
            self.instrucciones()
            self.state = 179
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
        self.enterRule(localctx, 40, self.RULE_comps)
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(compiladoresParser.MEN)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.match(compiladoresParser.MAY)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.match(compiladoresParser.MENI)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 184
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
        self.enterRule(localctx, 42, self.RULE_bools)
        try:
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(compiladoresParser.OR)
                self.state = 189
                self.factorBool()
                self.state = 190
                self.bools()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.match(compiladoresParser.AND)
                self.state = 193
                self.factorBool()
                self.state = 194
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
        self.enterRule(localctx, 44, self.RULE_factorBool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
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
        self.enterRule(localctx, 46, self.RULE_asignacionBool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(compiladoresParser.ID)
            self.state = 202
            self.match(compiladoresParser.ASIG)
            self.state = 203
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
        self.enterRule(localctx, 48, self.RULE_opbool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.factorBool()
            self.state = 206
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
        self.enterRule(localctx, 50, self.RULE_opcomp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(compiladoresParser.ID)
            self.state = 209
            self.comps()
            self.state = 210
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
        self.enterRule(localctx, 52, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(compiladoresParser.FOR)
            self.state = 213
            self.match(compiladoresParser.PA)
            self.state = 214
            self.init()
            self.state = 215
            self.match(compiladoresParser.PYC)
            self.state = 216
            self.cond()
            self.state = 217
            self.match(compiladoresParser.PYC)
            self.state = 218
            self.iter_()
            self.state = 219
            self.match(compiladoresParser.PC)
            self.state = 220
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
        self.enterRule(localctx, 54, self.RULE_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
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
        self.enterRule(localctx, 56, self.RULE_cond)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.opcomp()
                self.state = 225
                self.cond()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.opbool()
                self.state = 228
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
        self.enterRule(localctx, 58, self.RULE_iter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(compiladoresParser.ID)
            self.state = 234
            self.match(compiladoresParser.ASIG)
            self.state = 235
            self.match(compiladoresParser.ID)
            self.state = 236
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
        self.enterRule(localctx, 60, self.RULE_iteracion)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(compiladoresParser.SUMA)
                self.state = 239
                self.match(compiladoresParser.NUMERO)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.match(compiladoresParser.RESTA)
                self.state = 241
                self.match(compiladoresParser.NUMERO)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.match(compiladoresParser.MULT)
                self.state = 243
                self.match(compiladoresParser.NUMERO)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 244
                self.match(compiladoresParser.DIV)
                self.state = 245
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
        self.enterRule(localctx, 62, self.RULE_iif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(compiladoresParser.IF)
            self.state = 249
            self.match(compiladoresParser.PA)
            self.state = 250
            self.cond()
            self.state = 251
            self.match(compiladoresParser.PC)
            self.state = 252
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
        self.enterRule(localctx, 64, self.RULE_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(compiladoresParser.ELSE)
            self.state = 255
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
        self.enterRule(localctx, 66, self.RULE_eelse)
        try:
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.iif()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
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
        self.enterRule(localctx, 68, self.RULE_funciones)
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 25, 26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.tipoDatos()
                self.state = 262
                self.match(compiladoresParser.ID)
                self.state = 263
                self.match(compiladoresParser.PA)
                self.state = 264
                self.argumentos()
                self.state = 265
                self.match(compiladoresParser.PC)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.match(compiladoresParser.VOID)
                self.state = 268
                self.match(compiladoresParser.ID)
                self.state = 269
                self.match(compiladoresParser.PA)
                self.state = 270
                self.argumentos()
                self.state = 271
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
        self.enterRule(localctx, 70, self.RULE_argumentos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.argumento()
            self.state = 276
            self.arg()
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
        self.enterRule(localctx, 72, self.RULE_arg)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(compiladoresParser.COMA)
                self.state = 279
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
        self.enterRule(localctx, 74, self.RULE_argumento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.tipoDatos()
            self.state = 284
            self.match(compiladoresParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





