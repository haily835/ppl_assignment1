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
    elif tk == self.STRING:
        endPos = len(result.text) - 1
        result.text = result.text[1:endPos]
        return result
    else:
        return result;
}

options {
	language = Python3;
}

program: VAR COLON ID SEMI STRING EOF;

// IDENTIFIERS
ID: ~[0][a-z][a-zA-Z0-9_]*;

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
PLUS: '+';
F_PLUS: '+.';
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
O_BR: '(';
C_BR: ')';
O_SB: '[';
C_SB: ']';
O_CB: '{';
C_CB: '}';
DOT: '.';
COMMA: ',';

// LITERALS
fragment DEC:  [+-]?[1-9]+ | '0'+;
fragment HEX: '0'[Xx][0-9A-F]+;
fragment OCT: '0'[Oo][0-7]+;
INT: DEC | HEX | OCT;

fragment DIGIT: [0-9];
FLOAT: [+-]?(DIGIT+ '.' DIGIT+ | DIGIT+[Ee][+-]DIGIT+ | DIGIT+'.'DIGIT+[Ee][+-]DIGIT+);

BOOL: TRUE|FALSE;

STRING: '"' ([a-zA-Z0-9 ] | '\'"' | '\\' ['bfrnt\\])* '"';

ARRAY: '{' (BOOL* | INT* | FLOAT* | STRING* | ARRAY*) '}';

// LEXICAL ERRORS
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
ERROR_CHAR: .;
ILLEGAL_ESCAPE: '"' [a-zA-Z0-9 ]* '\\' ~[btfrn'\\] '"'?;
UNCLOSE_STRING: '"' ( [a-zA-Z0-9 ] | '\'"' | '\\' [btfrn\\])*;
UNTERMINATED_COMMENT: .;
