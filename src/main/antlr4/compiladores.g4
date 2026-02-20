grammar compiladores;

// --- LEXER ---
INT: 'int';
BOOL: 'bool';
FLOAT: 'float';
DOUBLE: 'double';
VOID: 'void';
WHILE: 'while';
FOR: 'for';
IF: 'if';
ELSE: 'else';
RETURN: 'return';
TRUE: 'TRUE';
FALSE: 'FALSE';

PA : '('; 
PC : ')'; 
PYC : ';';
LLA : '{';
LLC : '}';
COMA: ',';
PUNTO: '.';
ASIG : '=';

IGUAL : '==';
SUMA: '+' ;
RESTA: '-' ;
MULT: '*' ;
DIV: '/' ;
MOD: '%' ;
MAY: '>' ;
MEN: '<' ;
MAYI: '>=' ;
MENI: '<=' ;
OR: '||' ;
AND: '&&' ;

ID: [a-zA-Z_] [a-zA-Z0-9_]* ; 
NUMERO : [0-9]+ ;
DECIMAL : [0-9]+ '.' [0-9]+ | '.' [0-9]+ | [0-9]+ '.' ;

WS: [ \t\n\r]+ -> skip;
COMENTARIO: '//' ~[\r\n]* -> skip; 

// --- PARSER ---

programa: instrucciones EOF;

instrucciones: instruccion* ;

instruccion 
    : declaracionGlobal    // Maneja int a; y int funcion()...
    | funcionVoid          // Maneja void main()...
    | iwhile
    | ifor
    | iif
    | asignacionPYC
    | returnfun PYC
    | llamadafun
    | bloque
    ;

// --- RESOLUCIÓN DE CONFLICTO (Vital) ---
// Leemos TIPO e ID primero, luego decidimos si es función o variable
declaracionGlobal: tipoDatos ID restoDeclaracion;

restoDeclaracion
    : PA argumentos PC bloque   // Si sigue un '(', es función
    | PA argumentos PC PYC      // Prototipo con tipo
    | listaVars                 // Si sigue ',' o ';', es variable
    | asignacionInit            // Si sigue '=', es inicialización
    ;

listaVars: (COMA ID)* PYC;
asignacionInit: ASIG exp PYC;

funcionVoid
    : VOID ID PA argumentos PC bloque //Funcion void normal
    | VOID ID PA argumentos PC PYC     // Prototipo void
    ;

// --- ESTRUCTURAS ---
tipoDatos: BOOL | INT | FLOAT | DOUBLE ; 

argumento: tipoDatos ID;
argumentos: (argumento (COMA argumento)*)? ; 

// Corrección: bloque ya NO puede ser una instrucción suelta para evitar ciclos
bloque : LLA instrucciones LLC;

// --- RESTO ---
declaracion : tipoDatos ID (COMA ID)* ; 
declaracionPYC: declaracion PYC;

inic: tipoDatos asignacionNum PYC | tipoDatos asignacionBool PYC;

asignacionNum : ID ASIG exp;
asignacionBool : ID ASIG opbool;
asignacion : asignacionNum | asignacionBool;
asignacionPYC: asignacion PYC;

iwhile : WHILE PA cond PC bloque;
ifor : FOR PA init PYC cond PYC iter PC bloque;
init : asignacionNum;
iter: ID ASIG ID iteracion; 
iteracion: (SUMA|RESTA|MULT|DIV) NUMERO;
iif: IF PA cond PC bloque (ELSE bloque)?;

returnfun: RETURN exp | RETURN;

ids: (exp (COMA exp)*)? ; 
funcionVar: ID PA ids PC;
llamadafun: funcionVar PYC;

exp: term expPrima*; 
expPrima: (SUMA|RESTA) term;
term: factor t*;
t   : (MULT|DIV|MOD) factor;
factor: NUMERO | DECIMAL | ID | funcionVar | PA exp PC;

opcomp : ID (MEN | MAY | MENI | MAYI | IGUAL) factor;
opbool : (TRUE | FALSE) ( (OR|AND) (TRUE|FALSE) )*; 
cond : opcomp | opbool;