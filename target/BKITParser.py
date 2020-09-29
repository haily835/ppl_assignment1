# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\f\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2")
        buf.write("\2\n\2\4\3\2\2\2\4\5\7\4\2\2\5\6\7\61\2\2\6\7\7\3\2\2")
        buf.write("\7\b\7\60\2\2\b\t\7=\2\2\t\n\7\2\2\3\n\3\3\2\2\2\2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Var'", "'Body'", "'Break'", 
                     "'Continue'", "'Do'", "'Else'", "'ElseIf'", "'EndBody'", 
                     "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
                     "'If'", "'Parameter'", "'Return'", "'Then'", "'While'", 
                     "'True'", "'False'", "'EndDo'", "'+'", "'+.'", "'-'", 
                     "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", 
                     "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", 
                     "';'", "':'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "ID", "VAR", "BODY", "BREAK", "CONTINUE", 
                      "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
                      "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                      "RETURN", "THEN", "WHILE", "TRUE", "FALSE", "ENDDO", 
                      "PLUS", "F_PLUS", "SUB", "F_SUB", "MUL", "F_MUL", 
                      "DIV", "F_DIV", "REMAIN", "NEG", "AND", "OR", "EQ", 
                      "NOT_EQ", "LT", "GT", "LTE", "GTE", "F_NOT_EQ", "F_LT", 
                      "F_GT", "F_LTE", "F_GTE", "SEMI", "COLON", "O_BR", 
                      "C_BR", "O_SB", "C_SB", "O_CB", "C_CB", "DOT", "COMMA", 
                      "INT", "FLOAT", "BOOL", "STRING", "ARRAY", "WS", "ERROR_CHAR", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    ID=1
    VAR=2
    BODY=3
    BREAK=4
    CONTINUE=5
    DO=6
    ELSE=7
    ELSEIF=8
    ENDBODY=9
    ENDIF=10
    ENDFOR=11
    ENDWHILE=12
    FOR=13
    FUNCTION=14
    IF=15
    PARAMETER=16
    RETURN=17
    THEN=18
    WHILE=19
    TRUE=20
    FALSE=21
    ENDDO=22
    PLUS=23
    F_PLUS=24
    SUB=25
    F_SUB=26
    MUL=27
    F_MUL=28
    DIV=29
    F_DIV=30
    REMAIN=31
    NEG=32
    AND=33
    OR=34
    EQ=35
    NOT_EQ=36
    LT=37
    GT=38
    LTE=39
    GTE=40
    F_NOT_EQ=41
    F_LT=42
    F_GT=43
    F_LTE=44
    F_GTE=45
    SEMI=46
    COLON=47
    O_BR=48
    C_BR=49
    O_SB=50
    C_SB=51
    O_CB=52
    C_CB=53
    DOT=54
    COMMA=55
    INT=56
    FLOAT=57
    BOOL=58
    STRING=59
    ARRAY=60
    WS=61
    ERROR_CHAR=62
    ILLEGAL_ESCAPE=63
    UNCLOSE_STRING=64
    UNTERMINATED_COMMENT=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(BKITParser.VAR)
            self.state = 3
            self.match(BKITParser.COLON)
            self.state = 4
            self.match(BKITParser.ID)
            self.state = 5
            self.match(BKITParser.SEMI)
            self.state = 6
            self.match(BKITParser.STRING)
            self.state = 7
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





