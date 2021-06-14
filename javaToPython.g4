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

identifierDec:
	(identifierType)? ID (ASSIGN identifierInitializer)?;
identifierInitializer: minusOperator? expression;


statement_condition : statement_if
	| statement_elseif
	| statement_else;
statement_if: 	IF L_PAREN condition R_PAREN block;
statement_elseif: ELSEIF L_PAREN condition R_PAREN block;
statement_else: ELSE block;
block: 	L_BRACE statement* R_BRACE;
condition: expression compare expression
	| condition ((OR|AND) condition)
	| NOT condition
	| NOT expression
	| NOT value
	| value
	| minusOperator condition;
minusOperator: MINUS;

statement_for:	FOR L_PAREN assignment SEMICOLON expression_for SEMICOLON incr_for R_PAREN block;
expression_for: expression compare expression;
incr_for: ID INCR;
compare: GT	
	| LT	
	| EQ			
	| GT_EQ		
	| LT_EQ		
	| NEQ;
assignment: (identifierType)? ID ASSIGN identifierInitializer ;

statement_while: WHILE L_PAREN condition R_PAREN block;

statement_return: RETURN value;

methodDec: 	methodType ID L_PAREN params? R_PAREN block;
params:		identifierType ID (COMMA identifierType ID)*;

methodCall: 	ID L_PAREN expression (COMMA expression)* R_PAREN;

operacjeMatematyczne: identifierDec
	| incrementOperation SEMICOLON
	| decrementOperation SEMICOLON;
incrementOperation: INCR ID | ID INCR;
decrementOperation: DECR ID | ID DECR;

expression: L_PAREN expression R_PAREN
	| INT_VAL
	| FLOAT_VAL
	| STRING_VAL
	| CHAR_VAL
	| BOOLEAN_VAL
	| ID (L_BRACKET expression R_BRACKET)*
	| oneArgumentExpression
	| minusOperator expression
	| methodCall
	| expression (twoArgumentExpression|MINUS) expression ((twoArgumentExpression|MINUS) expression)*;

oneArgumentExpression: incrementOperation | decrementOperation | notOperation;

twoArgumentExpression: OR | AND | MUL | DIV | PLUS | MOD | GT | LT | EQ | GT_EQ | LT_EQ;

notOperation: NOT ID;

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

WHITESPACE	:   (' ' | '\t' | '\r' | '\n') -> skip ;
PLUS		:	'+';
MINUS		:	'-';
MUL			:	'*';
DIV			:	'/';
MOD			:	'%';
ASSIGN		:	'=';

GT			:	'>';
LT			:	'<';
EQ			:	'==';
GT_EQ		:	'>=';
LT_EQ		:	'<=';
NEQ			:	'!=';

AND			:	'&&';
OR			:	'||';
NOT			:	'!';

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
DOT			:	'.';
QUOTE1		:	'\''; 
QUOTE2		:	'"';

FOR			:	'for';
WHILE		:	'while';
IF			: 	'if';
ELSE		:	'else';
ELSEIF		:	'else if';
BREAK		:	'break';
FUNCTION	: 	'function';
RETURN		: 	'return';

VOID		: 	'void';
INT			:	'int';
FLOAT		:	'float';
CHAR		:	'char';
STRING		: 	'string';
BOOLEAN		:	'boolean';

TRUE		:	'true';
FALSE		:	'false';

ID			:	[a-zA-Z] [a-zA-Z0-9_]*;
INT_VAL		: 	[0-9]+;
FLOAT_VAL	:	[0-9]+'.'[0-9]+;
STRING_VAL 	:	'"' (~["\\r\n])* '"';
CHAR_VAL	:	'\'' (~['\\r\n]) '\'';
BOOLEAN_VAL :	(TRUE|FALSE);