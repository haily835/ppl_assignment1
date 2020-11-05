grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    return result;
}

options{
	language=Python3;
}

program: ids;

ids: ID (',' ID)*; 



ID: [a-z]+ ;