# Generated from c:\Users\Admin\Desktop\ppl\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\4")
        buf.write("\16\b\1\4\2\t\2\4\3\t\3\3\2\3\2\3\3\6\3\13\n\3\r\3\16")
        buf.write("\3\f\2\2\4\3\3\5\4\3\2\3\3\2c|\2\16\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\3\7\3\2\2\2\5\n\3\2\2\2\7\b\7.\2\2\b\4\3\2\2\2")
        buf.write("\t\13\t\2\2\2\n\t\3\2\2\2\13\f\3\2\2\2\f\n\3\2\2\2\f\r")
        buf.write("\3\2\2\2\r\6\3\2\2\2\4\2\f\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    ID = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','" ]

    symbolicNames = [ "<INVALID>",
            "ID" ]

    ruleNames = [ "T__0", "ID" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        return result;


