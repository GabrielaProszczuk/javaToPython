grammar javaToPython;

start: (statement)* EOF;

statement: identifierDec SEMICOLON
	| statement_condition
	| statement_for
	| statement_while
	| statement_return SEMICOLON
	| methodDec
	| methodCall SEMICOLON
	| operacjeMatematyczne;
	
operacjeMatematyczne: identifierDec
	| incrementOperation SEMICOLON
	| decrementOperation SEMICOLON;

identifierDec:
	(identifierType)? ID (ASSIGN identifierInitializer)? ;

identifierInitializer:
	minusOperator? expression;

statement_condition : statement_if
	| statement_elseif
	| statement_else;


statement_if: 	IF L_PAREN conditions R_PAREN block;

statement_elseif: ELSEIF L_PAREN conditions R_PAREN block;

statement_else: ELSE block;

block: 	L_BRACE statement* R_BRACE;

compare: GT	
	| LT	
	| EQ			
	| GT_EQ		
	| LT_EQ		
	| NEQ;



conditions: condition (cos condition)*;
condition: expression compare expression
	| NOT toNot
	| NOT toNot
	| NOT toNot
	| value
	| minusOperator condition;
cos: orOperation
	| andOperation;
toNot: condition
	| expression
	| value;
orOperation: OR;
andOperation: AND;	

statement_for:	FOR L_PAREN assignment SEMICOLON expression_for SEMICOLON oneArgumentExpression R_PAREN block;

expression_for: expression compare expression;

statement_while: WHILE L_PAREN conditions R_PAREN block;
statement_return: RETURN value;

assignment: (identifierType)? ID ASSIGN identifierInitializer ;


methodDec: 	methodType ID L_PAREN params? R_PAREN block;

params:		identifierType ID (COMMA identifierType ID)*;

methodCall: 	ID L_PAREN expression (COMMA expression)* R_PAREN;

	
minusOperator: MINUS;

oneArgumentExpression: incrementOperation | decrementOperation | notOperation;
twoArgumentExpression: MUL | DIV | PLUS | MOD | GT | LT | EQ | GT_EQ | LT_EQ;
incrementOperation: INCR ID | ID INCR;
decrementOperation: DECR ID | ID DECR;
notOperation: NOT ID;

expression: L_PAREN expression R_PAREN
	| INT_VAL
	| FLOAT_VAL
	| STRING_VAL
	| CHAR_VAL
	| ID (L_BRACKET expression R_BRACKET)*
	| oneArgumentExpression
	| minusOperator expression
	| methodCall
	| expression (twoArgumentExpression|MINUS) expression ((twoArgumentExpression|MINUS) expression)*;

value: 	INT_VAL 
	| FLOAT_VAL 
	| STRING_VAL
	| CHAR_VAL
	| BOOLEAN_VAL
	| ID;

identifierType: BOOLEAN
		| INT
		| FLOAT
		| CHAR
		| STRING;

methodType:	BOOLEAN
		| INT
		| FLOAT
		| VOID
		| STRING
		| CHAR;

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

TRUE		:    	'true';
FALSE		:   	'false';

ID		:	[a-zA-Z] [a-zA-Z0-9_]*;
INT_VAL		: 	[0-9]+;
FLOAT_VAL	:	[0-9]+'.'[0-9]+;
STRING_VAL :  	 '"' (~["])* '"';
CHAR_VAL	:	  '\'' (~[']) '\'';
BOOLEAN_VAL : (TRUE|FALSE);