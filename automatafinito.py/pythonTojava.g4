grammar PythonToJava;

prog_main: (define_funcion | sent)*;

define_funcion: 'def' NOMBRE '(' parametros? ')' ':' sent*;

parametros: NOMBRE (',' NOMBRE)*;

sent: asignacion_var | retorno | imprimir;

asignacion_var: NOMBRE '=' expresion;

retorno: 'return' expresion;

imprimir: 'print' '(' expresion (',' expresion)* ')';

expresion: expresion ('+'|'-'|'*'|'/') expresion
         | NUMERO
         | NOMBRE
         | NOMBRE '(' expresion (',' expresion)* ')'
         | '(' expresion ')';

NOMBRE: [a-zA-Z_][a-zA-Z_0-9]*;
NUMERO: [0-9]+;

ESPACIOS: [ \\t\\r\\n]+ -> skip;
"""

