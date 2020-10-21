# Generated from c:\Users\haigo\Desktop\initial\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("Q\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\6\2\31\n\2\r\2")
        buf.write("\16\2\32\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\7\6+\n\6\f\6\16\6.\13\6\3\6\3\6\3\7\6\7\63")
        buf.write("\n\7\r\7\16\7\64\3\7\3\7\3\b\3\b\3\t\3\t\7\t=\n\t\f\t")
        buf.write("\16\t@\13\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\7\nK\n")
        buf.write("\n\f\n\16\nN\13\n\3\13\3\13\2\2\f\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\3\2\7\3\2c|\6\2\"\"\62;C\\c")
        buf.write("|\b\2^^ddhhppttvv\5\2\13\f\17\17\"\"\t\2))^^ddhhppttv")
        buf.write("v\2Y\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\3\30\3\2\2\2\5\34\3\2\2\2\7\36\3")
        buf.write("\2\2\2\t \3\2\2\2\13$\3\2\2\2\r\62\3\2\2\2\178\3\2\2\2")
        buf.write("\21:\3\2\2\2\23D\3\2\2\2\25O\3\2\2\2\27\31\t\2\2\2\30")
        buf.write("\27\3\2\2\2\31\32\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2")
        buf.write("\33\4\3\2\2\2\34\35\7=\2\2\35\6\3\2\2\2\36\37\7<\2\2\37")
        buf.write("\b\3\2\2\2 !\7X\2\2!\"\7c\2\2\"#\7t\2\2#\n\3\2\2\2$,\7")
        buf.write("$\2\2%+\t\3\2\2&\'\7)\2\2\'+\7$\2\2()\7^\2\2)+\t\4\2\2")
        buf.write("*%\3\2\2\2*&\3\2\2\2*(\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-\3")
        buf.write("\2\2\2-/\3\2\2\2.,\3\2\2\2/\60\7$\2\2\60\f\3\2\2\2\61")
        buf.write("\63\t\5\2\2\62\61\3\2\2\2\63\64\3\2\2\2\64\62\3\2\2\2")
        buf.write("\64\65\3\2\2\2\65\66\3\2\2\2\66\67\b\7\2\2\67\16\3\2\2")
        buf.write("\289\13\2\2\29\20\3\2\2\2:>\7$\2\2;=\t\3\2\2<;\3\2\2\2")
        buf.write("=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?A\3\2\2\2@>\3\2\2\2AB\7")
        buf.write("^\2\2BC\n\6\2\2C\22\3\2\2\2DL\7$\2\2EK\t\3\2\2FG\7)\2")
        buf.write("\2GK\7$\2\2HI\7^\2\2IK\t\4\2\2JE\3\2\2\2JF\3\2\2\2JH\3")
        buf.write("\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\24\3\2\2\2NL\3\2")
        buf.write("\2\2OP\13\2\2\2P\26\3\2\2\2\n\2\32*,\64>JL\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    SEMI = 2
    COLON = 3
    VAR = 4
    STRING = 5
    WS = 6
    ERROR_CHAR = 7
    ILLEGAL_ESCAPE = 8
    UNCLOSE_STRING = 9
    UNTERMINATED_COMMENT = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':'", "'Var'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "SEMI", "COLON", "VAR", "STRING", "WS", "ERROR_CHAR", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "ID", "SEMI", "COLON", "VAR", "STRING", "WS", "ERROR_CHAR", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT" ]

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


