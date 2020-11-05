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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\4")
        buf.write("\21\4\2\t\2\4\3\t\3\3\2\3\2\3\3\3\3\3\3\7\3\f\n\3\f\3")
        buf.write("\16\3\17\13\3\3\3\2\2\4\2\4\2\2\2\17\2\6\3\2\2\2\4\b\3")
        buf.write("\2\2\2\6\7\5\4\3\2\7\3\3\2\2\2\b\r\7\4\2\2\t\n\7\3\2\2")
        buf.write("\n\f\7\4\2\2\13\t\3\2\2\2\f\17\3\2\2\2\r\13\3\2\2\2\r")
        buf.write("\16\3\2\2\2\16\5\3\2\2\2\17\r\3\2\2\2\3\r")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ID" ]

    RULE_program = 0
    RULE_ids = 1

    ruleNames =  [ "program", "ids" ]

    EOF = Token.EOF
    T__0=1
    ID=2

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ids(self):
            return self.getTypedRuleContext(BKITParser.IdsContext,0)


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
            self.state = 4
            self.ids()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ID)
            else:
                return self.getToken(BKITParser.ID, i)

        def getRuleIndex(self):
            return BKITParser.RULE_ids

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds" ):
                return visitor.visitIds(self)
            else:
                return visitor.visitChildren(self)




    def ids(self):

        localctx = BKITParser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ids)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(BKITParser.ID)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.T__0:
                self.state = 7
                self.match(BKITParser.T__0)
                self.state = 8
                self.match(BKITParser.ID)
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





