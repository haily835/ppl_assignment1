// Student ID: 1852348

grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text[1:])
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text[1:])
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    elif tk == self.STRING_LIT:
        endPos = len(result.text) - 1
        result.text = result.text[1:endPos]
        return result
    else:
        return result;
}

options {
	language = Python3;
}

// KEYWORDS
VAR: 'Var';
BODY: 'Body';
BREAK: 'Break';
CONTINUE: 'Continue';
DO: 'Do';
ELSE: 'Else';
ELSEIF: 'ElseIf';
ENDBODY: 'EndBody';
ENDIF: 'EndIf';
ENDFOR: 'EndFor';
ENDWHILE: 'EndWhile';
FOR: 'For';
FUNCTION: 'Function';
IF: 'If';
PARAMETER: 'Parameter';
RETURN: 'Return';
THEN: 'Then';
WHILE: 'While';
fragment TRUE: 'True';
fragment FALSE: 'False';
ENDDO: 'EndDo';

// OPERATORS
ADD: '+';
F_ADD: '+.';
SUB: '-';
F_SUB: '-.';
MUL: '*';
F_MUL: '*.';
DIV: '\\';
F_DIV: '\\.';
REMAIN: '%';
NEG: '!';
AND: '&&';
OR: '||';
EQ: '==';
NOT_EQ: '!=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';
F_NOT_EQ: '=/=';
F_LT: '<.';
F_GT: '>.';
F_LTE: '<=.';
F_GTE: '>=.';

// SEPARATORS
SEMI: ';';
COLON: ':';
LP: '(';
RP: ')';
LS: '[';
RS: ']';
LB: '{';
RB: '}';
DOT: '.';
COMMA: ',';

// IDENTIFIERS
ID: [a-z][a-zA-Z0-9_]*;

fragment DIGIT: [0-9];

// LITERALS

fragment DEC:  [1-9] DIGIT* | '0'+;
fragment HEX: '0' [Xx] [1-9A-F][0-9A-F]*;
fragment OCT: '0' [Oo] [1-7][0-7]*;

INT_LIT: DEC | HEX | OCT;

FLOAT_LIT:  (
            DIGIT+ '.' DIGIT* 
            | DIGIT+ [Ee] [+-]? DIGIT+ 
            | DIGIT+ '.' DIGIT* [Ee] [+-]? DIGIT+
            );

BOOL_LIT: TRUE | FALSE;

fragment ESC: '\\' ['bfrnt\\] | '\'"';
fragment STR_CHAR: ~[\n"'\\];
STRING_LIT: '"' (STR_CHAR | ESC )* '"';

array_lit: LB ( |
             BOOL_LIT  ( COMMA  BOOL_LIT  )*
            | INT_LIT ( COMMA  INT_LIT )*
            | FLOAT_LIT ( COMMA FLOAT_LIT )*
            | STRING_LIT ( COMMA STRING_LIT)*
            | array_lit ( COMMA  array_lit )*
            ) RB;


WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
COMMENT: '**' .*? '**' -> skip; // skip comment

// LEXICAL ERRORS
ERROR_CHAR: .;
ILLEGAL_ESCAPE: '"' (STR_CHAR | ESC )* ('\\' ~[btfrn'\\] | '\'' ~["]) '"'?;
UNCLOSE_STRING: '"' (STR_CHAR | ESC )*;
UNTERMINATED_COMMENT: '**' .*?;

// expression
relational_op: EQ | NOT_EQ | LT | GT | LTE | GTE | F_NOT_EQ | F_LT | F_GT | F_LTE | F_GTE;
logical_op: AND | OR;
adding_op: ADD | F_ADD | SUB | F_SUB;
multiplying_op: MUL | F_MUL | DIV | F_DIV | REMAIN;
sign_op: SUB | F_SUB;

argList: (expr tailArg)?;
tailArg: (COMMA expr tailArg)?;

expr: expr1 relational_op expr1 | expr1;
expr1: expr1 logical_op expr2 | expr2;
expr2: expr2 adding_op expr3 | expr3;
expr3: expr3 multiplying_op expr4 | expr4;
expr4: NEG expr4 | expr5;
expr5: sign_op expr5 | expr6;
expr6: expr6 index_op | expr7;
index_op: LS expr RS | LS expr RS index_op;
expr7: ID LP argList RP | term;
term: LP expr RP | INT_LIT | FLOAT_LIT | STRING_LIT | array_lit | BOOL_LIT | ID ;

program: globalVar funcDeclPart mainFunc EOF;

globalVar: (varDecl)*;
funcDeclPart: (funcDecl)*;

// Variable declaration
varDecl: VAR COLON varList SEMI;
varList: varInit (COMMA varInit)*;
varInit: variable ('=' (INT_LIT | FLOAT_LIT | BOOL_LIT | STRING_LIT | array_lit))?;
variable: ID | ID (LS INT_LIT RS)+;

// Function declaration 
funcDecl: FUNCTION COLON ID (paraDecl)? body;

paraDecl: PARAMETER COLON paraList;
paraList: variable (COMMA variable)*;

body: BODY COLON stmtList ENDBODY DOT;
mainFunc: FUNCTION COLON 'main' (paraDecl)? body;

// Statements
otherStmt: assignStmt | ifStmt | forStmt | whileStmt | dowhileStmt | breakStmt | continueStmt | callStmt | returnStmt;

assignStmt: variable '=' expr SEMI;
ifStmt: IF expr THEN stmtList (ELSEIF expr THEN stmtList)* (ELSE stmtList)? ENDIF DOT;
forStmt: FOR LP ID '=' expr COMMA expr COMMA expr RP DO stmtList ENDFOR DOT;
whileStmt: WHILE expr DO stmtList ENDWHILE DOT;
dowhileStmt: DO stmtList WHILE expr ENDDO DOT;
breakStmt: BREAK SEMI;
continueStmt: CONTINUE SEMI;
callStmt: ID LP argList RP SEMI;
returnStmt: RETURN (expr)? SEMI;

stmtList: varDecl* otherStmt*;