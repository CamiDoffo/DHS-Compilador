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
WHILE: 'while';
FOR: 'for';
IF: 'if';

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
instruccion : declaracion
            | iwhile
            | ifor
            | iif
            | bloque
            | inst
            ;

declaracion : INT ID PYC
            | BOOL ID PYC
            ;

asignacionInt : ID ASIG exp;

asignacion : ID ASIG opal;

inst : asignacion PYC; //asignacion completa

opal : exp
     | opbool
     ; //COMPLETAR, exp es solo una expresion aritmetica (TODO operaciones booleanas?)

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
      | PA exp PC
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
init : asignacionInt;
cond : opcomp cond// si quiero que la condicion tenga una operacion algebraica DEBE ESTAR ENTRE PARENTESIS
      | opbool cond
      |
      ;
iter: asignacion; //i = i+1;
iif: IF PA cond PC bloque;