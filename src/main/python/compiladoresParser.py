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
        4,1,37,369,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        108,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,117,8,3,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,133,8,4,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,147,8,6,1,7,1,7,1,7,1,8,
        1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,3,10,163,8,10,1,11,
        1,11,1,11,1,12,1,12,3,12,170,8,12,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,1,16,
        1,16,3,16,192,8,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,210,8,18,1,19,1,19,1,19,
        3,19,215,8,19,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,3,21,225,8,
        21,1,22,1,22,1,22,3,22,230,8,22,1,23,1,23,1,23,1,23,1,23,1,23,1,
        24,1,24,1,24,1,24,1,24,3,24,243,8,24,1,25,1,25,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,26,3,26,256,8,26,1,27,1,27,1,28,1,28,1,
        28,1,28,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,
        31,1,31,1,31,3,31,278,8,31,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,
        33,1,33,1,33,1,33,1,33,1,33,3,33,293,8,33,1,34,1,34,1,34,1,34,1,
        34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,3,34,308,8,34,1,35,1,
        35,1,35,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,3,37,322,8,
        37,1,38,1,38,1,38,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,41,1,41,3,
        41,336,8,41,1,42,1,42,1,42,1,42,3,42,342,8,42,1,43,1,43,1,43,1,43,
        1,44,1,44,1,44,1,44,1,44,1,44,1,45,1,45,1,46,1,46,1,46,1,46,3,46,
        360,8,46,1,47,1,47,1,47,3,47,365,8,47,1,48,1,48,1,48,0,0,49,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,
        94,96,0,4,1,0,24,27,2,0,23,23,34,35,2,0,9,9,15,18,1,0,21,22,358,
        0,98,1,0,0,0,2,107,1,0,0,0,4,109,1,0,0,0,6,116,1,0,0,0,8,132,1,0,
        0,0,10,134,1,0,0,0,12,146,1,0,0,0,14,148,1,0,0,0,16,151,1,0,0,0,
        18,153,1,0,0,0,20,162,1,0,0,0,22,164,1,0,0,0,24,169,1,0,0,0,26,171,
        1,0,0,0,28,181,1,0,0,0,30,183,1,0,0,0,32,191,1,0,0,0,34,193,1,0,
        0,0,36,209,1,0,0,0,38,214,1,0,0,0,40,216,1,0,0,0,42,224,1,0,0,0,
        44,229,1,0,0,0,46,231,1,0,0,0,48,242,1,0,0,0,50,244,1,0,0,0,52,255,
        1,0,0,0,54,257,1,0,0,0,56,259,1,0,0,0,58,263,1,0,0,0,60,266,1,0,
        0,0,62,277,1,0,0,0,64,279,1,0,0,0,66,292,1,0,0,0,68,307,1,0,0,0,
        70,309,1,0,0,0,72,312,1,0,0,0,74,321,1,0,0,0,76,323,1,0,0,0,78,326,
        1,0,0,0,80,328,1,0,0,0,82,335,1,0,0,0,84,341,1,0,0,0,86,343,1,0,
        0,0,88,347,1,0,0,0,90,353,1,0,0,0,92,359,1,0,0,0,94,364,1,0,0,0,
        96,366,1,0,0,0,98,99,3,2,1,0,99,100,5,0,0,1,100,1,1,0,0,0,101,102,
        5,1,0,0,102,103,3,2,1,0,103,104,5,2,0,0,104,105,3,2,1,0,105,108,
        1,0,0,0,106,108,1,0,0,0,107,101,1,0,0,0,107,106,1,0,0,0,108,3,1,
        0,0,0,109,110,3,6,3,0,110,111,5,0,0,1,111,5,1,0,0,0,112,113,3,8,
        4,0,113,114,3,6,3,0,114,117,1,0,0,0,115,117,1,0,0,0,116,112,1,0,
        0,0,116,115,1,0,0,0,117,7,1,0,0,0,118,133,3,18,9,0,119,133,3,46,
        23,0,120,133,3,26,13,0,121,133,3,68,34,0,122,133,3,22,11,0,123,133,
        3,86,43,0,124,133,3,12,6,0,125,133,3,70,35,0,126,127,3,84,42,0,127,
        128,5,3,0,0,128,133,1,0,0,0,129,133,3,10,5,0,130,133,3,88,44,0,131,
        133,3,90,45,0,132,118,1,0,0,0,132,119,1,0,0,0,132,120,1,0,0,0,132,
        121,1,0,0,0,132,122,1,0,0,0,132,123,1,0,0,0,132,124,1,0,0,0,132,
        125,1,0,0,0,132,126,1,0,0,0,132,129,1,0,0,0,132,130,1,0,0,0,132,
        131,1,0,0,0,133,9,1,0,0,0,134,135,5,4,0,0,135,136,3,6,3,0,136,137,
        5,5,0,0,137,11,1,0,0,0,138,139,3,16,8,0,139,140,3,20,10,0,140,141,
        5,3,0,0,141,147,1,0,0,0,142,143,3,16,8,0,143,144,3,56,28,0,144,145,
        5,3,0,0,145,147,1,0,0,0,146,138,1,0,0,0,146,142,1,0,0,0,147,13,1,
        0,0,0,148,149,3,16,8,0,149,150,5,35,0,0,150,15,1,0,0,0,151,152,7,
        0,0,0,152,17,1,0,0,0,153,154,3,14,7,0,154,155,5,3,0,0,155,19,1,0,
        0,0,156,157,5,35,0,0,157,158,5,8,0,0,158,163,3,30,15,0,159,160,5,
        35,0,0,160,161,5,8,0,0,161,163,5,23,0,0,162,156,1,0,0,0,162,159,
        1,0,0,0,163,21,1,0,0,0,164,165,3,24,12,0,165,166,5,3,0,0,166,23,
        1,0,0,0,167,170,3,20,10,0,168,170,3,56,28,0,169,167,1,0,0,0,169,
        168,1,0,0,0,170,25,1,0,0,0,171,172,5,30,0,0,172,173,5,1,0,0,173,
        174,3,28,14,0,174,175,5,3,0,0,175,176,3,62,31,0,176,177,5,3,0,0,
        177,178,3,64,32,0,178,179,5,2,0,0,179,180,3,48,24,0,180,27,1,0,0,
        0,181,182,3,20,10,0,182,29,1,0,0,0,183,184,3,34,17,0,184,185,3,32,
        16,0,185,31,1,0,0,0,186,187,5,10,0,0,187,192,3,30,15,0,188,189,5,
        11,0,0,189,192,3,30,15,0,190,192,1,0,0,0,191,186,1,0,0,0,191,188,
        1,0,0,0,191,190,1,0,0,0,192,33,1,0,0,0,193,194,3,38,19,0,194,195,
        3,36,18,0,195,35,1,0,0,0,196,197,5,12,0,0,197,198,3,38,19,0,198,
        199,3,36,18,0,199,210,1,0,0,0,200,201,5,13,0,0,201,202,3,38,19,0,
        202,203,3,36,18,0,203,210,1,0,0,0,204,205,5,14,0,0,205,206,3,38,
        19,0,206,207,3,36,18,0,207,210,1,0,0,0,208,210,1,0,0,0,209,196,1,
        0,0,0,209,200,1,0,0,0,209,204,1,0,0,0,209,208,1,0,0,0,210,37,1,0,
        0,0,211,215,5,23,0,0,212,215,5,35,0,0,213,215,3,40,20,0,214,211,
        1,0,0,0,214,212,1,0,0,0,214,213,1,0,0,0,215,39,1,0,0,0,216,217,5,
        35,0,0,217,218,5,1,0,0,218,219,3,42,21,0,219,220,5,2,0,0,220,41,
        1,0,0,0,221,222,7,1,0,0,222,225,3,44,22,0,223,225,1,0,0,0,224,221,
        1,0,0,0,224,223,1,0,0,0,225,43,1,0,0,0,226,227,5,6,0,0,227,230,3,
        42,21,0,228,230,1,0,0,0,229,226,1,0,0,0,229,228,1,0,0,0,230,45,1,
        0,0,0,231,232,5,29,0,0,232,233,5,1,0,0,233,234,3,62,31,0,234,235,
        5,2,0,0,235,236,3,48,24,0,236,47,1,0,0,0,237,238,5,4,0,0,238,239,
        3,6,3,0,239,240,5,5,0,0,240,243,1,0,0,0,241,243,3,8,4,0,242,237,
        1,0,0,0,242,241,1,0,0,0,243,49,1,0,0,0,244,245,7,2,0,0,245,51,1,
        0,0,0,246,247,5,19,0,0,247,248,3,54,27,0,248,249,3,52,26,0,249,256,
        1,0,0,0,250,251,5,20,0,0,251,252,3,54,27,0,252,253,3,52,26,0,253,
        256,1,0,0,0,254,256,1,0,0,0,255,246,1,0,0,0,255,250,1,0,0,0,255,
        254,1,0,0,0,256,53,1,0,0,0,257,258,7,3,0,0,258,55,1,0,0,0,259,260,
        5,35,0,0,260,261,5,8,0,0,261,262,3,58,29,0,262,57,1,0,0,0,263,264,
        3,54,27,0,264,265,3,52,26,0,265,59,1,0,0,0,266,267,5,35,0,0,267,
        268,3,50,25,0,268,269,3,38,19,0,269,61,1,0,0,0,270,271,3,60,30,0,
        271,272,3,62,31,0,272,278,1,0,0,0,273,274,3,58,29,0,274,275,3,62,
        31,0,275,278,1,0,0,0,276,278,1,0,0,0,277,270,1,0,0,0,277,273,1,0,
        0,0,277,276,1,0,0,0,278,63,1,0,0,0,279,280,5,35,0,0,280,281,5,8,
        0,0,281,282,5,35,0,0,282,283,3,66,33,0,283,65,1,0,0,0,284,285,5,
        10,0,0,285,293,5,23,0,0,286,287,5,11,0,0,287,293,5,23,0,0,288,289,
        5,12,0,0,289,293,5,23,0,0,290,291,5,13,0,0,291,293,5,23,0,0,292,
        284,1,0,0,0,292,286,1,0,0,0,292,288,1,0,0,0,292,290,1,0,0,0,293,
        67,1,0,0,0,294,295,5,31,0,0,295,296,5,1,0,0,296,297,3,62,31,0,297,
        298,5,2,0,0,298,299,3,48,24,0,299,308,1,0,0,0,300,301,5,31,0,0,301,
        302,5,1,0,0,302,303,3,62,31,0,303,304,5,2,0,0,304,305,3,48,24,0,
        305,306,3,70,35,0,306,308,1,0,0,0,307,294,1,0,0,0,307,300,1,0,0,
        0,308,69,1,0,0,0,309,310,5,32,0,0,310,311,3,48,24,0,311,71,1,0,0,
        0,312,313,5,35,0,0,313,314,5,1,0,0,314,315,3,74,37,0,315,316,5,2,
        0,0,316,73,1,0,0,0,317,318,3,78,39,0,318,319,3,76,38,0,319,322,1,
        0,0,0,320,322,1,0,0,0,321,317,1,0,0,0,321,320,1,0,0,0,322,75,1,0,
        0,0,323,324,5,6,0,0,324,325,3,74,37,0,325,77,1,0,0,0,326,327,5,35,
        0,0,327,79,1,0,0,0,328,329,5,35,0,0,329,330,5,1,0,0,330,331,3,92,
        46,0,331,332,5,2,0,0,332,81,1,0,0,0,333,336,3,16,8,0,334,336,5,28,
        0,0,335,333,1,0,0,0,335,334,1,0,0,0,336,83,1,0,0,0,337,338,5,33,
        0,0,338,342,3,30,15,0,339,340,5,33,0,0,340,342,5,28,0,0,341,337,
        1,0,0,0,341,339,1,0,0,0,342,85,1,0,0,0,343,344,3,82,41,0,344,345,
        3,80,40,0,345,346,5,3,0,0,346,87,1,0,0,0,347,348,3,82,41,0,348,349,
        3,80,40,0,349,350,5,4,0,0,350,351,3,6,3,0,351,352,5,5,0,0,352,89,
        1,0,0,0,353,354,3,80,40,0,354,91,1,0,0,0,355,356,3,96,48,0,356,357,
        3,94,47,0,357,360,1,0,0,0,358,360,1,0,0,0,359,355,1,0,0,0,359,358,
        1,0,0,0,360,93,1,0,0,0,361,362,5,6,0,0,362,365,3,92,46,0,363,365,
        1,0,0,0,364,361,1,0,0,0,364,363,1,0,0,0,365,95,1,0,0,0,366,367,3,
        14,7,0,367,97,1,0,0,0,21,107,116,132,146,162,169,191,209,214,224,
        229,242,255,277,292,307,321,335,341,359,364
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
                     "'double'", "'void'", "'while'", "'for'", "'if'", "'else'", 
                     "'return'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "PYC", "LLA", "LLC", "COMA", 
                      "PUNTO", "ASIG", "IGUAL", "SUMA", "RESTA", "MULT", 
                      "DIV", "MOD", "MAY", "MEN", "MAYI", "MENI", "OR", 
                      "AND", "TRUE", "FALSE", "NUMERO", "INT", "BOOL", "FLOAT", 
                      "DOUBLE", "VOID", "WHILE", "FOR", "IF", "ELSE", "RETURN", 
                      "BOOLEANS", "ID", "WS", "OTRO" ]

    RULE_si = 0
    RULE_s = 1
    RULE_programa = 2
    RULE_instrucciones = 3
    RULE_instruccion = 4
    RULE_bloqueSolo = 5
    RULE_inic = 6
    RULE_declaracion = 7
    RULE_tipoDatos = 8
    RULE_declaracionPYC = 9
    RULE_asignacionNum = 10
    RULE_asignacionPYC = 11
    RULE_asignacion = 12
    RULE_ifor = 13
    RULE_init = 14
    RULE_exp = 15
    RULE_expPrima = 16
    RULE_term = 17
    RULE_t = 18
    RULE_factor = 19
    RULE_funcionVar = 20
    RULE_ids = 21
    RULE_iden = 22
    RULE_iwhile = 23
    RULE_bloque = 24
    RULE_comps = 25
    RULE_bools = 26
    RULE_factorBool = 27
    RULE_asignacionBool = 28
    RULE_opbool = 29
    RULE_opcomp = 30
    RULE_cond = 31
    RULE_iter = 32
    RULE_iteracion = 33
    RULE_iif = 34
    RULE_else = 35
    RULE_fexp = 36
    RULE_parametros = 37
    RULE_para = 38
    RULE_parametro = 39
    RULE_funcion = 40
    RULE_return = 41
    RULE_returnfun = 42
    RULE_protofun = 43
    RULE_deffuncion = 44
    RULE_llamadafun = 45
    RULE_argumentos = 46
    RULE_arg = 47
    RULE_argumento = 48

    ruleNames =  [ "si", "s", "programa", "instrucciones", "instruccion", 
                   "bloqueSolo", "inic", "declaracion", "tipoDatos", "declaracionPYC", 
                   "asignacionNum", "asignacionPYC", "asignacion", "ifor", 
                   "init", "exp", "expPrima", "term", "t", "factor", "funcionVar", 
                   "ids", "iden", "iwhile", "bloque", "comps", "bools", 
                   "factorBool", "asignacionBool", "opbool", "opcomp", "cond", 
                   "iter", "iteracion", "iif", "else", "fexp", "parametros", 
                   "para", "parametro", "funcion", "return", "returnfun", 
                   "protofun", "deffuncion", "llamadafun", "argumentos", 
                   "arg", "argumento" ]

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
    RETURN=33
    BOOLEANS=34
    ID=35
    WS=36
    OTRO=37

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
            self.state = 98
            self.s()
            self.state = 99
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
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.match(compiladoresParser.PA)
                self.state = 102
                self.s()
                self.state = 103
                self.match(compiladoresParser.PC)
                self.state = 104
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
            self.state = 109
            self.instrucciones()
            self.state = 110
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
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.instruccion()
                self.state = 113
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


        def asignacionPYC(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionPYCContext,0)


        def protofun(self):
            return self.getTypedRuleContext(compiladoresParser.ProtofunContext,0)


        def inic(self):
            return self.getTypedRuleContext(compiladoresParser.InicContext,0)


        def else_(self):
            return self.getTypedRuleContext(compiladoresParser.ElseContext,0)


        def returnfun(self):
            return self.getTypedRuleContext(compiladoresParser.ReturnfunContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def bloqueSolo(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueSoloContext,0)


        def deffuncion(self):
            return self.getTypedRuleContext(compiladoresParser.DeffuncionContext,0)


        def llamadafun(self):
            return self.getTypedRuleContext(compiladoresParser.LlamadafunContext,0)


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
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.declaracionPYC()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.iwhile()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.ifor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 121
                self.iif()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 122
                self.asignacionPYC()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 123
                self.protofun()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 124
                self.inic()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 125
                self.else_()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 126
                self.returnfun()
                self.state = 127
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 129
                self.bloqueSolo()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 130
                self.deffuncion()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 131
                self.llamadafun()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueSoloContext(ParserRuleContext):
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
            return compiladoresParser.RULE_bloqueSolo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloqueSolo" ):
                listener.enterBloqueSolo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloqueSolo" ):
                listener.exitBloqueSolo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloqueSolo" ):
                return visitor.visitBloqueSolo(self)
            else:
                return visitor.visitChildren(self)




    def bloqueSolo(self):

        localctx = compiladoresParser.BloqueSoloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_bloqueSolo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(compiladoresParser.LLA)
            self.state = 135
            self.instrucciones()
            self.state = 136
            self.match(compiladoresParser.LLC)
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
        self.enterRule(localctx, 12, self.RULE_inic)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.tipoDatos()
                self.state = 139
                self.asignacionNum()
                self.state = 140
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.tipoDatos()
                self.state = 143
                self.asignacionBool()
                self.state = 144
                self.match(compiladoresParser.PYC)
                pass


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
        self.enterRule(localctx, 14, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.tipoDatos()
            self.state = 149
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
        self.enterRule(localctx, 16, self.RULE_tipoDatos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
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
        self.enterRule(localctx, 18, self.RULE_declaracionPYC)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.declaracion()
            self.state = 154
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
        self.enterRule(localctx, 20, self.RULE_asignacionNum)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.match(compiladoresParser.ID)
                self.state = 157
                self.match(compiladoresParser.ASIG)
                self.state = 158
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(compiladoresParser.ID)
                self.state = 160
                self.match(compiladoresParser.ASIG)
                self.state = 161
                self.match(compiladoresParser.NUMERO)
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
        self.enterRule(localctx, 22, self.RULE_asignacionPYC)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.asignacion()
            self.state = 165
            self.match(compiladoresParser.PYC)
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
        self.enterRule(localctx, 24, self.RULE_asignacion)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.asignacionNum()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.asignacionBool()
                pass


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
        self.enterRule(localctx, 26, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(compiladoresParser.FOR)
            self.state = 172
            self.match(compiladoresParser.PA)
            self.state = 173
            self.init()
            self.state = 174
            self.match(compiladoresParser.PYC)
            self.state = 175
            self.cond()
            self.state = 176
            self.match(compiladoresParser.PYC)
            self.state = 177
            self.iter_()
            self.state = 178
            self.match(compiladoresParser.PC)
            self.state = 179
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
        self.enterRule(localctx, 28, self.RULE_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.asignacionNum()
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
        self.enterRule(localctx, 30, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.term()
            self.state = 184
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
        self.enterRule(localctx, 32, self.RULE_expPrima)
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.match(compiladoresParser.SUMA)
                self.state = 187
                self.exp()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(compiladoresParser.RESTA)
                self.state = 189
                self.exp()
                pass
            elif token in [3]:
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
        self.enterRule(localctx, 34, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.factor()
            self.state = 194
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
        self.enterRule(localctx, 36, self.RULE_t)
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.match(compiladoresParser.MULT)
                self.state = 197
                self.factor()
                self.state = 198
                self.t()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.match(compiladoresParser.DIV)
                self.state = 201
                self.factor()
                self.state = 202
                self.t()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.match(compiladoresParser.MOD)
                self.state = 205
                self.factor()
                self.state = 206
                self.t()
                pass
            elif token in [3, 10, 11]:
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

        def funcionVar(self):
            return self.getTypedRuleContext(compiladoresParser.FuncionVarContext,0)


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
        self.enterRule(localctx, 38, self.RULE_factor)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.funcionVar()
                pass


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
        self.enterRule(localctx, 40, self.RULE_funcionVar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(compiladoresParser.ID)
            self.state = 217
            self.match(compiladoresParser.PA)
            self.state = 218
            self.ids()
            self.state = 219
            self.match(compiladoresParser.PC)
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

        def iden(self):
            return self.getTypedRuleContext(compiladoresParser.IdenContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def BOOLEANS(self):
            return self.getToken(compiladoresParser.BOOLEANS, 0)

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
        self.enterRule(localctx, 42, self.RULE_ids)
        self._la = 0 # Token type
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 34, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 51547996160) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 222
                self.iden()
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


    class IdenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladoresParser.COMA, 0)

        def ids(self):
            return self.getTypedRuleContext(compiladoresParser.IdsContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_iden

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIden" ):
                listener.enterIden(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIden" ):
                listener.exitIden(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIden" ):
                return visitor.visitIden(self)
            else:
                return visitor.visitChildren(self)




    def iden(self):

        localctx = compiladoresParser.IdenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_iden)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(compiladoresParser.COMA)
                self.state = 227
                self.ids()
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
        self.enterRule(localctx, 46, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(compiladoresParser.WHILE)
            self.state = 232
            self.match(compiladoresParser.PA)
            self.state = 233
            self.cond()
            self.state = 234
            self.match(compiladoresParser.PC)
            self.state = 235
            self.bloque()
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

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


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
        self.enterRule(localctx, 48, self.RULE_bloque)
        try:
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(compiladoresParser.LLA)
                self.state = 238
                self.instrucciones()
                self.state = 239
                self.match(compiladoresParser.LLC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.instruccion()
                pass


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

        def IGUAL(self):
            return self.getToken(compiladoresParser.IGUAL, 0)

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
        self.enterRule(localctx, 50, self.RULE_comps)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 492032) != 0)):
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
        self.enterRule(localctx, 52, self.RULE_bools)
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(compiladoresParser.OR)
                self.state = 247
                self.factorBool()
                self.state = 248
                self.bools()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(compiladoresParser.AND)
                self.state = 251
                self.factorBool()
                self.state = 252
                self.bools()
                pass
            elif token in [2, 3, 21, 22, 35]:
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
        self.enterRule(localctx, 54, self.RULE_factorBool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
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
        self.enterRule(localctx, 56, self.RULE_asignacionBool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(compiladoresParser.ID)
            self.state = 260
            self.match(compiladoresParser.ASIG)
            self.state = 261
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
        self.enterRule(localctx, 58, self.RULE_opbool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.factorBool()
            self.state = 264
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
        self.enterRule(localctx, 60, self.RULE_opcomp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(compiladoresParser.ID)
            self.state = 267
            self.comps()
            self.state = 268
            self.factor()
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
        self.enterRule(localctx, 62, self.RULE_cond)
        try:
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.opcomp()
                self.state = 271
                self.cond()
                pass
            elif token in [21, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.opbool()
                self.state = 274
                self.cond()
                pass
            elif token in [2, 3]:
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
        self.enterRule(localctx, 64, self.RULE_iter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(compiladoresParser.ID)
            self.state = 280
            self.match(compiladoresParser.ASIG)
            self.state = 281
            self.match(compiladoresParser.ID)
            self.state = 282
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
        self.enterRule(localctx, 66, self.RULE_iteracion)
        try:
            self.state = 292
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.match(compiladoresParser.SUMA)
                self.state = 285
                self.match(compiladoresParser.NUMERO)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.match(compiladoresParser.RESTA)
                self.state = 287
                self.match(compiladoresParser.NUMERO)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 288
                self.match(compiladoresParser.MULT)
                self.state = 289
                self.match(compiladoresParser.NUMERO)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 290
                self.match(compiladoresParser.DIV)
                self.state = 291
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


        def else_(self):
            return self.getTypedRuleContext(compiladoresParser.ElseContext,0)


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
        self.enterRule(localctx, 68, self.RULE_iif)
        try:
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(compiladoresParser.IF)
                self.state = 295
                self.match(compiladoresParser.PA)
                self.state = 296
                self.cond()
                self.state = 297
                self.match(compiladoresParser.PC)
                self.state = 298
                self.bloque()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.match(compiladoresParser.IF)
                self.state = 301
                self.match(compiladoresParser.PA)
                self.state = 302
                self.cond()
                self.state = 303
                self.match(compiladoresParser.PC)
                self.state = 304
                self.bloque()
                self.state = 305
                self.else_()
                pass


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

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


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
        self.enterRule(localctx, 70, self.RULE_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(compiladoresParser.ELSE)
            self.state = 310
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def parametros(self):
            return self.getTypedRuleContext(compiladoresParser.ParametrosContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_fexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFexp" ):
                listener.enterFexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFexp" ):
                listener.exitFexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFexp" ):
                return visitor.visitFexp(self)
            else:
                return visitor.visitChildren(self)




    def fexp(self):

        localctx = compiladoresParser.FexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_fexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(compiladoresParser.ID)
            self.state = 313
            self.match(compiladoresParser.PA)
            self.state = 314
            self.parametros()
            self.state = 315
            self.match(compiladoresParser.PC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametro(self):
            return self.getTypedRuleContext(compiladoresParser.ParametroContext,0)


        def para(self):
            return self.getTypedRuleContext(compiladoresParser.ParaContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = compiladoresParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_parametros)
        try:
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.parametro()
                self.state = 318
                self.para()
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


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladoresParser.COMA, 0)

        def parametros(self):
            return self.getTypedRuleContext(compiladoresParser.ParametrosContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_para

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPara" ):
                listener.enterPara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPara" ):
                listener.exitPara(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = compiladoresParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(compiladoresParser.COMA)
            self.state = 324
            self.parametros()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametro" ):
                return visitor.visitParametro(self)
            else:
                return visitor.visitChildren(self)




    def parametro(self):

        localctx = compiladoresParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_parametro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(compiladoresParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def argumentos(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentosContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)




    def funcion(self):

        localctx = compiladoresParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(compiladoresParser.ID)
            self.state = 329
            self.match(compiladoresParser.PA)
            self.state = 330
            self.argumentos()
            self.state = 331
            self.match(compiladoresParser.PC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipoDatos(self):
            return self.getTypedRuleContext(compiladoresParser.TipoDatosContext,0)


        def VOID(self):
            return self.getToken(compiladoresParser.VOID, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)




    def return_(self):

        localctx = compiladoresParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_return)
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 25, 26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.tipoDatos()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.match(compiladoresParser.VOID)
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


    class ReturnfunContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(compiladoresParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def VOID(self):
            return self.getToken(compiladoresParser.VOID, 0)

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
        self.enterRule(localctx, 84, self.RULE_returnfun)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(compiladoresParser.RETURN)
                self.state = 338
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.match(compiladoresParser.RETURN)
                self.state = 340
                self.match(compiladoresParser.VOID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProtofunContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_(self):
            return self.getTypedRuleContext(compiladoresParser.ReturnContext,0)


        def funcion(self):
            return self.getTypedRuleContext(compiladoresParser.FuncionContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_protofun

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtofun" ):
                listener.enterProtofun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtofun" ):
                listener.exitProtofun(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProtofun" ):
                return visitor.visitProtofun(self)
            else:
                return visitor.visitChildren(self)




    def protofun(self):

        localctx = compiladoresParser.ProtofunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_protofun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.return_()
            self.state = 344
            self.funcion()
            self.state = 345
            self.match(compiladoresParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeffuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_(self):
            return self.getTypedRuleContext(compiladoresParser.ReturnContext,0)


        def funcion(self):
            return self.getTypedRuleContext(compiladoresParser.FuncionContext,0)


        def LLA(self):
            return self.getToken(compiladoresParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def LLC(self):
            return self.getToken(compiladoresParser.LLC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_deffuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeffuncion" ):
                listener.enterDeffuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeffuncion" ):
                listener.exitDeffuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeffuncion" ):
                return visitor.visitDeffuncion(self)
            else:
                return visitor.visitChildren(self)




    def deffuncion(self):

        localctx = compiladoresParser.DeffuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_deffuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.return_()
            self.state = 348
            self.funcion()
            self.state = 349
            self.match(compiladoresParser.LLA)
            self.state = 350
            self.instrucciones()
            self.state = 351
            self.match(compiladoresParser.LLC)
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

        def funcion(self):
            return self.getTypedRuleContext(compiladoresParser.FuncionContext,0)


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
        self.enterRule(localctx, 90, self.RULE_llamadafun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.funcion()
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
        self.enterRule(localctx, 92, self.RULE_argumentos)
        try:
            self.state = 359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 25, 26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.argumento()
                self.state = 356
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
        self.enterRule(localctx, 94, self.RULE_arg)
        try:
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.match(compiladoresParser.COMA)
                self.state = 362
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

        def declaracion(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionContext,0)


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
        self.enterRule(localctx, 96, self.RULE_argumento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.declaracion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





