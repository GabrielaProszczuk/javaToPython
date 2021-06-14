// stara wersja
grammar javaToPython;

start: (statement)* EOF;
value: 	INT_VAL 
	| FLOAT_VAL 
	| STRING_VAL
	| CHAR_VAL
	| BOOLEAN_VAL
	| ID;

expOperation: 	PLUS
		| MINUS
		| MUL
		| DIV
		| MOD;


expression: 	NOT value
		| value (expOperation value)*;


methodType:	BOOLEAN
		| INT
		| FLOAT
		| VOID
		| STRING
		| CHAR;

identifierType: BOOLEAN
		| INT
		| FLOAT
		| CHAR
		| STRING;

identifierDec: 	identifierType ID;

assignment: 	identifierType ID ASSIGN value
		| ID ASSIGN value
		| ID ASSIGN expression
		| ID (INCR|DECR)
		| (INCR|DECR) ID;

methodDec: 	methodType ID L_PAREN params? R_PAREN block;

params:		identifierType ID (COMMA identifierType ID)*;

compare: GT	
	| LT	
	| EQ			
	| GT_EQ		
	| LT_EQ		
	| NEQ;	

condition: value compare value
	| condition ((OR|AND) condition)+
	| NOT condition
	| NOT value
	| value;

block: 	L_BRACE statement* R_BRACE;


methodCall: 	ID L_PAREN value (COMMA value)* R_PAREN;

statement_for:	FOR L_PAREN assignment SEMICOLON condition SEMICOLON assignment R_PAREN block;

statement_while: WHILE L_PAREN condition R_PAREN block;

statement_condition : statement_if
	| statement_elseif
	| statement_else;

statement_if: 	IF L_PAREN condition R_PAREN block;

statement_elseif: ELSEIF L_PAREN condition R_PAREN block;

statement_else: ELSE block;



statement_return: RETURN value;



statement: 	assignment SEMICOLON	
		| expression SEMICOLON
		| statement_for
		| statement_condition
		| statement_return SEMICOLON
		| statement_while
		| methodDec
		| methodCall SEMICOLON
		| identifierDec SEMICOLON 
		| block;


WHITESPACE:         (' ' | '\t' | '\r' | '\n') -> skip ;
PLUS		:	'+';
MINUS		:	'-';
MUL		:	'*';
DIV		:	'/';
MOD		:	'%';
ASSIGN		:	'=';

GT		:	'>';
LT		:	'<';
EQ		:	'==';
GT_EQ		:	'>=';
LT_EQ		:	'<=';
NEQ		:	'!=';

AND		:	'&&';
OR		:	'||';
NOT		:	'!';

INCR		:	'++';
DECR		:	'--';

L_PAREN		:	'(';
R_PAREN		:	')';
L_BRACKET	:	'[';
R_BRACKET	:	']';
L_BRACE		:	'{';
R_BRACE		:	'}';


SEMICOLON	:	';';
COMMA		:	',';
DOT		:	'.';
QUOTE1		:	'\''; 
QUOTE2		:	'"';



FOR		:	'for';
WHILE		:	'while';
IF		: 	'if';
ELSE		:	'else';
ELSEIF		:	'else if';
BREAK		:	'break';
FUNCTION	: 	'function';
RETURN		: 	'return';

VOID		: 	'void';
INT		:       'int';
FLOAT		:	'float';
CHAR		:	'char';
STRING		: 	'string';
BOOLEAN		:	'boolean';

PRIVATE		:   	'private';
PUBLIC		:     	'public';
TRUE		:    	'true';
FALSE		:   	'false';

ID		:	[a-zA-Z] [a-zA-Z0-9_]*;
INT_VAL		: 	[0-9]+;
FLOAT_VAL	:	[0-9]+'.'[0-9]+;
STRING_VAL :  	 '"' (~["\\r\n])* '"';
CHAR_VAL	:	  '\'' (~['\\r\n]) '\'';
BOOLEAN_VAL : (TRUE|FALSE);