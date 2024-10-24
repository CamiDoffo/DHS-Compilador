grammar compiladores;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

PA : '('; //esto puede ser una expresion especifica
PC : ')';
PYC : ';';
LLA : '{';
LLC : '}';

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

TRUE: 'true';
FALSE: 'false';

NUMERO : DIGITO+ ;

INT: 'int';
BOOL: 'bool';
FLOAT: 'float';
DOUBLE: 'double';
//float: (NUMERO).(NUMERO); //NOSE LOCO

WHILE: 'while';
FOR: 'for';
IF: 'if';
ELSE: 'else';

BOOLEANS: TRUE
        | FALSE
        ;

ID: (LETRA | '_')(LETRA | DIGITO | '_')*; //expresion regular

WS: [ \t\n\r] -> skip;
OTRO : . ;//por si no entra en ninguna regla; si no esta esto lo toma como un error lexico


// s : ID     {print("ID ->" + $ID.text + "<--") }         s
//   | NUMERO {print("NUMERO ->" + $NUMERO.text + "<--") } s
//   | OTRO   {print("Otro ->" + $OTRO.text + "<--") }     s
//   | EOF
//   ;

// analisis sintactico:
si : s EOF; //veo desde la raiz; simbolo inicial

s : PA s PC s
  |
  ;

programa: instrucciones EOF;

instrucciones : instruccion instrucciones
              |
              ;
instruccion : declaracionPYC
            | iwhile
            | ifor
            | iif
            | bloque
            | inst
            ;
inic: tipoDatos asignacion;
declaracion : tipoDatos ID;
tipoDatos: BOOL
          | INT
          | FLOAT
          | DOUBLE
          ; 
declaracionPYC: declaracion PYC;
asignacionNum : ID ASIG exp
              | ID ASIG NUMERO
              ;

asignacion : ID ASIG opal
            | ID ASIG NUMERO
            | ID ASIG BOOLEANS
            ;

inst : asignacion PYC; //asignacion completa

opal : exp
     | opbool
     ;

exp: term expPrima ;

expPrima: SUMA term expPrima
        | RESTA term expPrima
        | //Esto es una regla vacia, para cuando no hay mas terminos para operar
        ;

term: factor t ;
t    : MULT factor t
    | DIV factor t
    | MOD factor t
    |
    ;
factor: NUMERO
      | ID
      | PA exp PC //sin parentesis no le gusta TODO preguntar profe
      ;

iwhile : WHILE PA ID PC instruccion;

bloque : LLA instrucciones LLC;

comps: MEN
      | MAY
      | MENI
      | MAYI
      |
      ;
bools: OR factorBool bools
      | AND factorBool bools
      |
      ;
factorBool: ID
          | TRUE
          | FALSE
          ;
asignacionBool : ID ASIG opbool;
opbool : factorBool bools ;
opcomp : ID comps factor;

ifor : FOR PA init PYC cond PYC iter PC bloque;
init : asignacionNum;
cond : opcomp cond// si quiero que la condicion tenga una operacion algebraica DEBE ESTAR ENTRE PARENTESIS
      | opbool cond
      |
      ;
iter: asignacion; //i = i+1;
iif: IF PA cond PC bloque;
else: ELSE eelse;
eelse: iif
     | bloque
     ; 