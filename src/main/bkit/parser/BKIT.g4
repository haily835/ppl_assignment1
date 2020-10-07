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
    elif tk == self.ERROR_INTLIT:
        raise ErrorToken(result.text)
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
TRUE: 'True';
FALSE: 'False';
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

// SEPAERATORS
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
literals: INT_LIT | FLOAT_LIT | ARRAY_LIT | STRING_LIT;
fragment DEC:  [+-]? [1-9] DIGIT* | '0';
fragment HEX: '0' [Xx] [0-9A-F]+;
fragment OCT: '0' [Oo] [0-7]+;

INT_LIT: DEC | HEX | OCT;

FLOAT_LIT:  [+-]?(
            DIGIT+ '.' DIGIT+ 
            | DIGIT+ [Ee] [+-] DIGIT+ 
            | DIGIT+ '.' DIGIT+ [Ee] [+-] DIGIT+
            );

BOOL_LIT: TRUE | FALSE;

fragment ESC: '\\' ['bfrnt\\];
STRING_LIT: '"' ([a-zA-Z0-9 ] | '\'"' | ESC )* '"';

ARRAY_LIT: LB 
            ( ' '* BOOL_LIT ' '* ( ' '* COMMA ' '* BOOL_LIT ' '* )*
            | ' '* INT_LIT ' '* ( ' '* COMMA ' '*  INT_LIT ' '* )*
            | ' '* FLOAT_LIT ' '*  ( ' '* COMMA ' '* FLOAT_LIT ' '* )*
            | ' '* STRING_LIT ' '* ( ' '* COMMA ' '* STRING_LIT ' '* )*
            | ' '* ARRAY_LIT ' '* ( ' '* COMMA ' '*  ARRAY_LIT ' '* )* )
            RB;


WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
COMMENT: '**' .*? '**' -> skip; // skip comment

// LEXICAL ERRORS
ERROR_CHAR: .;
ILLEGAL_ESCAPE: '"' [a-zA-Z0-9 ]* '\\' ~[btfrn'\\] '"'?;
UNCLOSE_STRING: '"' ( [a-zA-Z0-9 ] | '\'"' | '\\' [btfrn'\\])*;
UNTERMINATED_COMMENT: '**' .*?;
ERROR_INTLIT: '0'[Xx] ~[A-F0-9]* | '0'[Oo] ~[0-7]*;


// expression
relational_op: EQ | NOT_EQ | LT | GT | LTE | GTE | F_NOT_EQ | F_LT | F_GT | F_LTE | F_GTE;
logical_op: AND | OR;
adding_op: ADD | F_ADD | SUB | F_SUB;
multiplying_op: MUL | F_MUL | DIV | F_DIV | REMAIN;
sign_op: SUB | F_SUB;

// expr: expr1 RELATIONAL_OP epxr1 | expr1;
// expr1: expr1 LOGICAL_OP expr2 | expr2;
// expr2: expr2 ADDING_OP expr3 | expr3;
// epxr3: expr3 MULTIPLYING_OP expr4 | expr4;
// expr4: NEG expr4 | expr5;
// expr5: (ID idx_op) | expr6;
// idx_op: '[' (expr5 | INT_LIT | ID) ']' | idx_op '[' (expr5 | INT_LIT | ID) ']';
// expr6: ID LP argList RP | term; // function call

argList: (expr tailArg)?;
tailArg: (COMMA expr tailArg)?;

indexing: LS (expr | INT_LIT | ID) RS;
expr: LB expr RB
    | ID LP argList RP // function call
    | ID (indexing)+ // indexing
    | <assoc=right> sign_op expr
    | <assoc=right> NEG expr
    | expr multiplying_op expr
    | expr adding_op expr
    | expr logical_op expr
    | expr relational_op expr
    | literals
    ;

program: globalVar funcDeclPart mainFunc EOF;

globalVar: (varDecl)*;
funcDeclPart: (funcDecl)*;
mainFunc: FUNCTION COLON 'main' body DOT;

// Variable declaration
varDecl: VAR COLON varList SEMI;
varList: varInit (COMMA varList)*;
varInit: variable ('=' (INT_LIT | FLOAT_LIT | TRUE | FALSE | STRING_LIT | ARRAY_LIT))?;
variable: ID | ID (indexing)+;

// Function declaration 
funcDecl: FUNCTION COLON ID paraDecl body DOT;

paraDecl: PARAMETER COLON paraList;
paraList: para (COMMA paraList)*;
para: ID | ID (LS expr RS)+;

body: BODY COLON (varDecl)* (stmt)* ENDBODY;

stmt: varDecl | assignStmt;
assignStmt: variable '=' expr SEMI;
