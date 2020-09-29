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

ID: ~[0][a-z][a-zA-Z0-9_];

SEMI: ';';

COLON: ':';

VAR: 'Var';
 
KEY_WORD: ('Body' | 'Break' | 'Continue' | 'Do' | 'Else' | 'ElseIf' | 'EndBody' | 'EndIf' | 'EndFor' | 'EndWhile' | 'For' | 'Function' | 'If' | 'Parameter' | 'Return' | 'Then' | 'Var' | 'While' | 'True' | 'False' | 'EndDo' );

OPERATOR: ('+'|'+.'|'-'|'-.'|'*'|'*.'|'\\'|'\\.'|'%'|'!'|'&&'|'||'|'=='|'!='|'<'|'>'|'<='|'>='|'=/='|'<.'|'>.'|'<=.'|'>=.');

SEPARATOR: ('('|')'|'['|']'|'{'|'}'|SEMI|COLON|VAR);

fragment DEC: '0'+ | [+-]?[1-9]+;
fragment HEX: '0'[Xx][0-9A-F]+;
fragment OCT: '0'[Oo][0-7]+;
fragment INT: DEC | HEX | OCT;

fragment DIGIT: [0-9];
fragment FLOAT: [+-]?(DIGIT+ '.' DIGIT+ | DIGIT+[Ee][+-]DIGIT+ | DIGIT+'.'DIGIT+[Ee][+-]DIGIT+);

fragment BOOL: 'True'|'False';

fragment STRING: '"' ([a-zA-Z0-9 ] | '\'"' | '\\' ['bfrnt\\])* '"';

fragment ARRAY: '{' (BOOL* | INT* | FLOAT* | STRING* | ARRAY*) '}';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
ERROR_CHAR: .;
ILLEGAL_ESCAPE: '"' [a-zA-Z0-9 ]* '\\' ~[btfrn'\\];

UNCLOSE_STRING: '"' ( [a-zA-Z0-9 ] | '\'"' | '\\' [btfrn\\])*;
UNTERMINATED_COMMENT: .;
