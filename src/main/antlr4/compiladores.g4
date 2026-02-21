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
    : declaracionGlobal    // Maneja int a, b=2; y int funcion()...
    | funcionVoid          // Maneja void main()...
    | iwhile
    | ifor
    | iif
    | asignacionPYC
    | returnfun PYC
    | llamadafun
    | bloque
    ;

// --- RESOLUCIÓN DE CONFLICTO Y VARIABLES MÚLTIPLES ---
declaracionGlobal : tipoDatos ID restoDeclaracion;

restoDeclaracion
    : PA argumentos PC (bloque | PYC)       // Función normal o Prototipo
    | (ASIG exp)? (COMA decItem)* PYC       // Variables simples o múltiples
    ;

decItem : ID (ASIG exp)? ;

funcionVoid
    : VOID ID PA argumentos PC (bloque | PYC) // Función void normal o Prototipo
    ;

// --- ESTRUCTURAS ---
tipoDatos: BOOL | INT | FLOAT | DOUBLE ; 

argumento: tipoDatos ID;
argumentos: (argumento (COMA argumento)*)? ; 

bloque : LLA instrucciones LLC;
instruccionOBloque : bloque | instruccion ;

iwhile : WHILE PA exp PC instruccionOBloque;
iif: IF PA exp PC instruccionOBloque (ELSE instruccionOBloque)?;
ifor : FOR PA (tipoDatos? decItem) PYC exp PYC asignacion PC instruccionOBloque;

asignacion : ID ASIG exp;
asignacionPYC: asignacion PYC;

returnfun: RETURN exp | RETURN;

ids: (exp (COMA exp)*)? ; 
funcionVar: ID PA ids PC;
llamadafun: funcionVar PYC;

// --- EXPRESIÓN UNIFICADA (La Magia) ---
exp : exp (MULT | DIV | MOD) exp         // Prioridad 1: Matemáticas
    | exp (SUMA | RESTA) exp             // Prioridad 2: Matemáticas
    | exp (MAY | MEN | MAYI | IGUAL) exp // Prioridad 3: Comparaciones
    | exp AND exp                        // Prioridad 4: AND lógico
    | exp OR exp                         // Prioridad 5: OR lógico
    | factor
    ;

factor: NUMERO | DECIMAL | TRUE | FALSE | ID | funcionVar | PA exp PC;