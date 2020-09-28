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

ID: [a-z]+;

SEMI: ';';

COLON: ':';

VAR: 'Var';

STRING: '"' ([a-zA-Z0-9 ] | '\'"' | '\\' [btfrn\\])* '"';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
ERROR_CHAR: .;
ILLEGAL_ESCAPE: '"' [a-zA-Z0-9 ]* '\\' ~[btfrn'\\];

UNCLOSE_STRING: '"' ( [a-zA-Z0-9 ] | '\'"' | '\\' [btfrn\\])*;
UNTERMINATED_COMMENT: .;
