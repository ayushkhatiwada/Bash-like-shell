# Generated from CommandGrammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,146,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,3,0,26,8,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,38,8,1,1,2,1,2,3,2,42,8,2,
        1,2,1,2,1,2,1,2,3,2,48,8,2,1,3,5,3,51,8,3,10,3,12,3,54,9,3,1,3,1,
        3,5,3,58,8,3,10,3,12,3,61,9,3,5,3,63,8,3,10,3,12,3,66,9,3,1,3,1,
        3,5,3,70,8,3,10,3,12,3,73,9,3,1,3,5,3,76,8,3,10,3,12,3,79,9,3,1,
        3,5,3,82,8,3,10,3,12,3,85,9,3,1,4,1,4,1,4,3,4,90,8,4,1,5,1,5,4,5,
        94,8,5,11,5,12,5,95,1,5,1,5,1,6,1,6,4,6,102,8,6,11,6,12,6,103,1,
        6,1,6,1,7,1,7,1,7,5,7,111,8,7,10,7,12,7,114,9,7,1,7,1,7,1,8,1,8,
        3,8,120,8,8,1,9,1,9,4,9,124,8,9,11,9,12,9,125,1,10,1,10,5,10,130,
        8,10,10,10,12,10,133,9,10,1,10,1,10,1,10,5,10,138,8,10,10,10,12,
        10,141,9,10,1,10,3,10,144,8,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,
        18,20,0,3,2,0,2,2,8,8,1,0,7,8,2,0,3,3,7,8,160,0,25,1,0,0,0,2,37,
        1,0,0,0,4,41,1,0,0,0,6,52,1,0,0,0,8,89,1,0,0,0,10,91,1,0,0,0,12,
        99,1,0,0,0,14,107,1,0,0,0,16,119,1,0,0,0,18,123,1,0,0,0,20,143,1,
        0,0,0,22,26,3,2,1,0,23,26,3,4,2,0,24,26,3,6,3,0,25,22,1,0,0,0,25,
        23,1,0,0,0,25,24,1,0,0,0,25,26,1,0,0,0,26,27,1,0,0,0,27,28,5,0,0,
        1,28,1,1,0,0,0,29,30,3,6,3,0,30,31,5,1,0,0,31,32,3,6,3,0,32,38,1,
        0,0,0,33,34,3,6,3,0,34,35,5,1,0,0,35,36,3,2,1,0,36,38,1,0,0,0,37,
        29,1,0,0,0,37,33,1,0,0,0,38,3,1,0,0,0,39,42,3,2,1,0,40,42,3,6,3,
        0,41,39,1,0,0,0,41,40,1,0,0,0,42,43,1,0,0,0,43,47,5,4,0,0,44,48,
        3,2,1,0,45,48,3,4,2,0,46,48,3,6,3,0,47,44,1,0,0,0,47,45,1,0,0,0,
        47,46,1,0,0,0,47,48,1,0,0,0,48,5,1,0,0,0,49,51,5,9,0,0,50,49,1,0,
        0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,64,1,0,0,0,54,52,
        1,0,0,0,55,59,3,20,10,0,56,58,5,9,0,0,57,56,1,0,0,0,58,61,1,0,0,
        0,59,57,1,0,0,0,59,60,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,62,55,
        1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,
        66,64,1,0,0,0,67,77,3,18,9,0,68,70,5,9,0,0,69,68,1,0,0,0,70,73,1,
        0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,71,1,0,0,0,74,
        76,3,16,8,0,75,71,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,
        0,0,78,83,1,0,0,0,79,77,1,0,0,0,80,82,5,9,0,0,81,80,1,0,0,0,82,85,
        1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,7,1,0,0,0,85,83,1,0,0,0,86,
        90,3,10,5,0,87,90,3,14,7,0,88,90,3,12,6,0,89,86,1,0,0,0,89,87,1,
        0,0,0,89,88,1,0,0,0,90,9,1,0,0,0,91,93,5,2,0,0,92,94,8,0,0,0,93,
        92,1,0,0,0,94,95,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,97,1,0,0,
        0,97,98,5,2,0,0,98,11,1,0,0,0,99,101,5,7,0,0,100,102,8,1,0,0,101,
        100,1,0,0,0,102,103,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,
        105,1,0,0,0,105,106,5,7,0,0,106,13,1,0,0,0,107,112,5,3,0,0,108,111,
        3,12,6,0,109,111,8,2,0,0,110,108,1,0,0,0,110,109,1,0,0,0,111,114,
        1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,115,1,0,0,0,114,112,
        1,0,0,0,115,116,5,3,0,0,116,15,1,0,0,0,117,120,3,20,10,0,118,120,
        3,18,9,0,119,117,1,0,0,0,119,118,1,0,0,0,120,17,1,0,0,0,121,124,
        3,8,4,0,122,124,5,11,0,0,123,121,1,0,0,0,123,122,1,0,0,0,124,125,
        1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,19,1,0,0,0,127,131,5,
        5,0,0,128,130,5,9,0,0,129,128,1,0,0,0,130,133,1,0,0,0,131,129,1,
        0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,131,1,0,0,0,134,144,3,
        18,9,0,135,139,5,6,0,0,136,138,5,9,0,0,137,136,1,0,0,0,138,141,1,
        0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,141,139,1,
        0,0,0,142,144,3,18,9,0,143,127,1,0,0,0,143,135,1,0,0,0,144,21,1,
        0,0,0,21,25,37,41,47,52,59,64,71,77,83,89,95,103,110,112,119,123,
        125,131,139,143
    ]

class CommandGrammarParser ( Parser ):

    grammarFileName = "CommandGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|'", "'''", "'\"'", "';'", "'<'", "'>'", 
                     "'`'", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "PIPE", "SINGLE_QUOTE", "DOUBLE_QUOTE", 
                      "SEMI_COLON", "LESS_THAN", "GREATER_THAN", "BACKQUOTE", 
                      "NEWLINE", "WHITESPACE", "NON_KEYWORD", "UNQUOTED" ]

    RULE_command = 0
    RULE_pipe = 1
    RULE_seq = 2
    RULE_call = 3
    RULE_quoted = 4
    RULE_singleQuoted = 5
    RULE_backQuoted = 6
    RULE_doubleQuoted = 7
    RULE_atom = 8
    RULE_argument = 9
    RULE_redirection = 10

    ruleNames =  [ "command", "pipe", "seq", "call", "quoted", "singleQuoted", 
                   "backQuoted", "doubleQuoted", "atom", "argument", "redirection" ]

    EOF = Token.EOF
    PIPE=1
    SINGLE_QUOTE=2
    DOUBLE_QUOTE=3
    SEMI_COLON=4
    LESS_THAN=5
    GREATER_THAN=6
    BACKQUOTE=7
    NEWLINE=8
    WHITESPACE=9
    NON_KEYWORD=10
    UNQUOTED=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CommandGrammarParser.EOF, 0)

        def pipe(self):
            return self.getTypedRuleContext(CommandGrammarParser.PipeContext,0)


        def seq(self):
            return self.getTypedRuleContext(CommandGrammarParser.SeqContext,0)


        def call(self):
            return self.getTypedRuleContext(CommandGrammarParser.CallContext,0)


        def getRuleIndex(self):
            return CommandGrammarParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = CommandGrammarParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 22
                self.pipe()

            elif la_ == 2:
                self.state = 23
                self.seq()

            elif la_ == 3:
                self.state = 24
                self.call()


            self.state = 27
            self.match(CommandGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandGrammarParser.CallContext)
            else:
                return self.getTypedRuleContext(CommandGrammarParser.CallContext,i)


        def PIPE(self):
            return self.getToken(CommandGrammarParser.PIPE, 0)

        def pipe(self):
            return self.getTypedRuleContext(CommandGrammarParser.PipeContext,0)


        def getRuleIndex(self):
            return CommandGrammarParser.RULE_pipe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPipe" ):
                listener.enterPipe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPipe" ):
                listener.exitPipe(self)




    def pipe(self):

        localctx = CommandGrammarParser.PipeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pipe)
        try:
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.call()
                self.state = 30
                self.match(CommandGrammarParser.PIPE)
                self.state = 31
                self.call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.call()
                self.state = 34
                self.match(CommandGrammarParser.PIPE)
                self.state = 35
                self.pipe()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI_COLON(self):
            return self.getToken(CommandGrammarParser.SEMI_COLON, 0)

        def pipe(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandGrammarParser.PipeContext)
            else:
                return self.getTypedRuleContext(CommandGrammarParser.PipeContext,i)


        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandGrammarParser.CallContext)
            else:
                return self.getTypedRuleContext(CommandGrammarParser.CallContext,i)


        def seq(self):
            return self.getTypedRuleContext(CommandGrammarParser.SeqContext,0)


        def getRuleIndex(self):
            return CommandGrammarParser.RULE_seq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeq" ):
                listener.enterSeq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeq" ):
                listener.exitSeq(self)




    def seq(self):

        localctx = CommandGrammarParser.SeqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_seq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 39
                self.pipe()
                pass

            elif la_ == 2:
                self.state = 40
                self.call()
                pass


            self.state = 43
            self.match(CommandGrammarParser.SEMI_COLON)
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 44
                self.pipe()

            elif la_ == 2:
                self.state = 45
                self.seq()

            elif la_ == 3:
                self.state = 46
                self.call()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(CommandGrammarParser.ArgumentContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.WHITESPACE)
            else:
                return self.getToken(CommandGrammarParser.WHITESPACE, i)

        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandGrammarParser.RedirectionContext)
            else:
                return self.getTypedRuleContext(CommandGrammarParser.RedirectionContext,i)


        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandGrammarParser.AtomContext)
            else:
                return self.getTypedRuleContext(CommandGrammarParser.AtomContext,i)


        def getRuleIndex(self):
            return CommandGrammarParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = CommandGrammarParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 49
                self.match(CommandGrammarParser.WHITESPACE)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 55
                self.redirection()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 56
                    self.match(CommandGrammarParser.WHITESPACE)
                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.argument()
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==9:
                        self.state = 68
                        self.match(CommandGrammarParser.WHITESPACE)
                        self.state = 73
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 74
                    self.atom() 
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 80
                self.match(CommandGrammarParser.WHITESPACE)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleQuoted(self):
            return self.getTypedRuleContext(CommandGrammarParser.SingleQuotedContext,0)


        def doubleQuoted(self):
            return self.getTypedRuleContext(CommandGrammarParser.DoubleQuotedContext,0)


        def backQuoted(self):
            return self.getTypedRuleContext(CommandGrammarParser.BackQuotedContext,0)


        def getRuleIndex(self):
            return CommandGrammarParser.RULE_quoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuoted" ):
                listener.enterQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuoted" ):
                listener.exitQuoted(self)




    def quoted(self):

        localctx = CommandGrammarParser.QuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_quoted)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.singleQuoted()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.doubleQuoted()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.backQuoted()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.SINGLE_QUOTE)
            else:
                return self.getToken(CommandGrammarParser.SINGLE_QUOTE, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.NEWLINE)
            else:
                return self.getToken(CommandGrammarParser.NEWLINE, i)

        def getRuleIndex(self):
            return CommandGrammarParser.RULE_singleQuoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleQuoted" ):
                listener.enterSingleQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleQuoted" ):
                listener.exitSingleQuoted(self)




    def singleQuoted(self):

        localctx = CommandGrammarParser.SingleQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_singleQuoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(CommandGrammarParser.SINGLE_QUOTE)
            self.state = 93 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 92
                _la = self._input.LA(1)
                if _la <= 0 or _la==2 or _la==8:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 95 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3834) != 0)):
                    break

            self.state = 97
            self.match(CommandGrammarParser.SINGLE_QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BackQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BACKQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.BACKQUOTE)
            else:
                return self.getToken(CommandGrammarParser.BACKQUOTE, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.NEWLINE)
            else:
                return self.getToken(CommandGrammarParser.NEWLINE, i)

        def getRuleIndex(self):
            return CommandGrammarParser.RULE_backQuoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBackQuoted" ):
                listener.enterBackQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBackQuoted" ):
                listener.exitBackQuoted(self)




    def backQuoted(self):

        localctx = CommandGrammarParser.BackQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_backQuoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(CommandGrammarParser.BACKQUOTE)
            self.state = 101 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 100
                _la = self._input.LA(1)
                if _la <= 0 or _la==7 or _la==8:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 103 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3710) != 0)):
                    break

            self.state = 105
            self.match(CommandGrammarParser.BACKQUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoubleQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.DOUBLE_QUOTE)
            else:
                return self.getToken(CommandGrammarParser.DOUBLE_QUOTE, i)

        def backQuoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandGrammarParser.BackQuotedContext)
            else:
                return self.getTypedRuleContext(CommandGrammarParser.BackQuotedContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.NEWLINE)
            else:
                return self.getToken(CommandGrammarParser.NEWLINE, i)

        def BACKQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.BACKQUOTE)
            else:
                return self.getToken(CommandGrammarParser.BACKQUOTE, i)

        def getRuleIndex(self):
            return CommandGrammarParser.RULE_doubleQuoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoubleQuoted" ):
                listener.enterDoubleQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoubleQuoted" ):
                listener.exitDoubleQuoted(self)




    def doubleQuoted(self):

        localctx = CommandGrammarParser.DoubleQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_doubleQuoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(CommandGrammarParser.DOUBLE_QUOTE)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3830) != 0):
                self.state = 110
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7]:
                    self.state = 108
                    self.backQuoted()
                    pass
                elif token in [1, 2, 4, 5, 6, 9, 10, 11]:
                    self.state = 109
                    _la = self._input.LA(1)
                    if _la <= 0 or (((_la) & ~0x3f) == 0 and ((1 << _la) & 392) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
            self.match(CommandGrammarParser.DOUBLE_QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def redirection(self):
            return self.getTypedRuleContext(CommandGrammarParser.RedirectionContext,0)


        def argument(self):
            return self.getTypedRuleContext(CommandGrammarParser.ArgumentContext,0)


        def getRuleIndex(self):
            return CommandGrammarParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = CommandGrammarParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_atom)
        try:
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.redirection()
                pass
            elif token in [2, 3, 7, 11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandGrammarParser.QuotedContext)
            else:
                return self.getTypedRuleContext(CommandGrammarParser.QuotedContext,i)


        def UNQUOTED(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.UNQUOTED)
            else:
                return self.getToken(CommandGrammarParser.UNQUOTED, i)

        def getRuleIndex(self):
            return CommandGrammarParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = CommandGrammarParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 123
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [2, 3, 7]:
                        self.state = 121
                        self.quoted()
                        pass
                    elif token in [11]:
                        self.state = 122
                        self.match(CommandGrammarParser.UNQUOTED)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 125 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RedirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS_THAN(self):
            return self.getToken(CommandGrammarParser.LESS_THAN, 0)

        def argument(self):
            return self.getTypedRuleContext(CommandGrammarParser.ArgumentContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandGrammarParser.WHITESPACE)
            else:
                return self.getToken(CommandGrammarParser.WHITESPACE, i)

        def GREATER_THAN(self):
            return self.getToken(CommandGrammarParser.GREATER_THAN, 0)

        def getRuleIndex(self):
            return CommandGrammarParser.RULE_redirection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRedirection" ):
                listener.enterRedirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRedirection" ):
                listener.exitRedirection(self)




    def redirection(self):

        localctx = CommandGrammarParser.RedirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(CommandGrammarParser.LESS_THAN)
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 128
                    self.match(CommandGrammarParser.WHITESPACE)
                    self.state = 133
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 134
                self.argument()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.match(CommandGrammarParser.GREATER_THAN)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 136
                    self.match(CommandGrammarParser.WHITESPACE)
                    self.state = 141
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 142
                self.argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





