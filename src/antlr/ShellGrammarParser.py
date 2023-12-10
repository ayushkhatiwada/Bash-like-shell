# Generated from ShellGrammar.g4 by ANTLR 4.13.1
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
        4,1,10,146,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,3,0,26,8,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,3,2,40,8,2,1,2,1,2,
        1,2,1,2,3,2,46,8,2,1,3,5,3,49,8,3,10,3,12,3,52,9,3,1,3,1,3,5,3,56,
        8,3,10,3,12,3,59,9,3,5,3,61,8,3,10,3,12,3,64,9,3,1,3,1,3,5,3,68,
        8,3,10,3,12,3,71,9,3,1,3,5,3,74,8,3,10,3,12,3,77,9,3,1,3,5,3,80,
        8,3,10,3,12,3,83,9,3,1,4,1,4,3,4,87,8,4,1,5,1,5,4,5,91,8,5,11,5,
        12,5,92,1,6,1,6,5,6,97,8,6,10,6,12,6,100,9,6,1,6,1,6,1,6,5,6,105,
        8,6,10,6,12,6,108,9,6,1,6,3,6,111,8,6,1,7,1,7,1,7,3,7,116,8,7,1,
        8,1,8,5,8,120,8,8,10,8,12,8,123,9,8,1,8,1,8,1,9,1,9,1,9,5,9,130,
        8,9,10,9,12,9,133,9,9,1,9,1,9,1,10,1,10,5,10,139,8,10,10,10,12,10,
        142,9,10,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,2,2,
        0,3,3,9,9,1,0,8,9,160,0,25,1,0,0,0,2,35,1,0,0,0,4,39,1,0,0,0,6,50,
        1,0,0,0,8,86,1,0,0,0,10,90,1,0,0,0,12,110,1,0,0,0,14,115,1,0,0,0,
        16,117,1,0,0,0,18,126,1,0,0,0,20,136,1,0,0,0,22,26,3,2,1,0,23,26,
        3,4,2,0,24,26,3,6,3,0,25,22,1,0,0,0,25,23,1,0,0,0,25,24,1,0,0,0,
        25,26,1,0,0,0,26,1,1,0,0,0,27,28,3,6,3,0,28,29,5,2,0,0,29,30,3,6,
        3,0,30,36,1,0,0,0,31,32,3,6,3,0,32,33,5,2,0,0,33,34,3,2,1,0,34,36,
        1,0,0,0,35,27,1,0,0,0,35,31,1,0,0,0,36,3,1,0,0,0,37,40,3,2,1,0,38,
        40,3,6,3,0,39,37,1,0,0,0,39,38,1,0,0,0,40,41,1,0,0,0,41,45,5,5,0,
        0,42,46,3,2,1,0,43,46,3,4,2,0,44,46,3,6,3,0,45,42,1,0,0,0,45,43,
        1,0,0,0,45,44,1,0,0,0,45,46,1,0,0,0,46,5,1,0,0,0,47,49,5,10,0,0,
        48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,62,1,
        0,0,0,52,50,1,0,0,0,53,57,3,12,6,0,54,56,5,10,0,0,55,54,1,0,0,0,
        56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,61,1,0,0,0,59,57,1,
        0,0,0,60,53,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,
        65,1,0,0,0,64,62,1,0,0,0,65,75,3,10,5,0,66,68,5,10,0,0,67,66,1,0,
        0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,69,
        1,0,0,0,72,74,3,8,4,0,73,69,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,
        75,76,1,0,0,0,76,81,1,0,0,0,77,75,1,0,0,0,78,80,5,10,0,0,79,78,1,
        0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,7,1,0,0,0,83,
        81,1,0,0,0,84,87,3,12,6,0,85,87,3,10,5,0,86,84,1,0,0,0,86,85,1,0,
        0,0,87,9,1,0,0,0,88,91,3,14,7,0,89,91,5,1,0,0,90,88,1,0,0,0,90,89,
        1,0,0,0,91,92,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,11,1,0,0,0,
        94,98,5,6,0,0,95,97,5,10,0,0,96,95,1,0,0,0,97,100,1,0,0,0,98,96,
        1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,98,1,0,0,0,101,111,3,10,
        5,0,102,106,5,7,0,0,103,105,5,10,0,0,104,103,1,0,0,0,105,108,1,0,
        0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,109,1,0,0,0,108,106,1,0,
        0,0,109,111,3,10,5,0,110,94,1,0,0,0,110,102,1,0,0,0,111,13,1,0,0,
        0,112,116,3,16,8,0,113,116,3,18,9,0,114,116,3,20,10,0,115,112,1,
        0,0,0,115,113,1,0,0,0,115,114,1,0,0,0,116,15,1,0,0,0,117,121,5,3,
        0,0,118,120,8,0,0,0,119,118,1,0,0,0,120,123,1,0,0,0,121,119,1,0,
        0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,121,1,0,0,0,124,125,5,3,
        0,0,125,17,1,0,0,0,126,131,5,4,0,0,127,130,3,20,10,0,128,130,8,1,
        0,0,129,127,1,0,0,0,129,128,1,0,0,0,130,133,1,0,0,0,131,129,1,0,
        0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,131,1,0,0,0,134,135,5,4,
        0,0,135,19,1,0,0,0,136,140,5,8,0,0,137,139,8,1,0,0,138,137,1,0,0,
        0,139,142,1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,143,1,0,0,
        0,142,140,1,0,0,0,143,144,5,8,0,0,144,21,1,0,0,0,21,25,35,39,45,
        50,57,62,69,75,81,86,90,92,98,106,110,115,121,129,131,140
    ]

class ShellGrammarParser ( Parser ):

    grammarFileName = "ShellGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'|'", "'''", "'\"'", "';'", 
                     "'<'", "'>'", "'`'", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "UNQUOTED", "PIPE", "SINGLE_QUOTE", "DOUBLE_QUOTE", 
                      "SEMI_COLON", "LESS_THAN", "GREATER_THAN", "BACKQUOTE", 
                      "NEWLINE", "WHITESPACE" ]

    RULE_command = 0
    RULE_pipe = 1
    RULE_seq = 2
    RULE_call = 3
    RULE_atom = 4
    RULE_argument = 5
    RULE_redirection = 6
    RULE_quoted = 7
    RULE_singleQuoted = 8
    RULE_doubleQuoted = 9
    RULE_backQuoted = 10

    ruleNames =  [ "command", "pipe", "seq", "call", "atom", "argument", 
                   "redirection", "quoted", "singleQuoted", "doubleQuoted", 
                   "backQuoted" ]

    EOF = Token.EOF
    UNQUOTED=1
    PIPE=2
    SINGLE_QUOTE=3
    DOUBLE_QUOTE=4
    SEMI_COLON=5
    LESS_THAN=6
    GREATER_THAN=7
    BACKQUOTE=8
    NEWLINE=9
    WHITESPACE=10

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

        def pipe(self):
            return self.getTypedRuleContext(ShellGrammarParser.PipeContext,0)


        def seq(self):
            return self.getTypedRuleContext(ShellGrammarParser.SeqContext,0)


        def call(self):
            return self.getTypedRuleContext(ShellGrammarParser.CallContext,0)


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = ShellGrammarParser.CommandContext(self, self._ctx, self.state)
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
                return self.getTypedRuleContexts(ShellGrammarParser.CallContext)
            else:
                return self.getTypedRuleContext(ShellGrammarParser.CallContext,i)


        def PIPE(self):
            return self.getToken(ShellGrammarParser.PIPE, 0)

        def pipe(self):
            return self.getTypedRuleContext(ShellGrammarParser.PipeContext,0)


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_pipe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPipe" ):
                listener.enterPipe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPipe" ):
                listener.exitPipe(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPipe" ):
                return visitor.visitPipe(self)
            else:
                return visitor.visitChildren(self)




    def pipe(self):

        localctx = ShellGrammarParser.PipeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pipe)
        try:
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.call()
                self.state = 28
                self.match(ShellGrammarParser.PIPE)
                self.state = 29
                self.call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.call()
                self.state = 32
                self.match(ShellGrammarParser.PIPE)
                self.state = 33
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
            return self.getToken(ShellGrammarParser.SEMI_COLON, 0)

        def pipe(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellGrammarParser.PipeContext)
            else:
                return self.getTypedRuleContext(ShellGrammarParser.PipeContext,i)


        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellGrammarParser.CallContext)
            else:
                return self.getTypedRuleContext(ShellGrammarParser.CallContext,i)


        def seq(self):
            return self.getTypedRuleContext(ShellGrammarParser.SeqContext,0)


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_seq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeq" ):
                listener.enterSeq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeq" ):
                listener.exitSeq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeq" ):
                return visitor.visitSeq(self)
            else:
                return visitor.visitChildren(self)




    def seq(self):

        localctx = ShellGrammarParser.SeqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_seq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 37
                self.pipe()
                pass

            elif la_ == 2:
                self.state = 38
                self.call()
                pass


            self.state = 41
            self.match(ShellGrammarParser.SEMI_COLON)
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 42
                self.pipe()

            elif la_ == 2:
                self.state = 43
                self.seq()

            elif la_ == 3:
                self.state = 44
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
            return self.getTypedRuleContext(ShellGrammarParser.ArgumentContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.WHITESPACE)
            else:
                return self.getToken(ShellGrammarParser.WHITESPACE, i)

        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellGrammarParser.RedirectionContext)
            else:
                return self.getTypedRuleContext(ShellGrammarParser.RedirectionContext,i)


        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellGrammarParser.AtomContext)
            else:
                return self.getTypedRuleContext(ShellGrammarParser.AtomContext,i)


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = ShellGrammarParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 47
                self.match(ShellGrammarParser.WHITESPACE)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 53
                self.redirection()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 54
                    self.match(ShellGrammarParser.WHITESPACE)
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.argument()
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==10:
                        self.state = 66
                        self.match(ShellGrammarParser.WHITESPACE)
                        self.state = 71
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 72
                    self.atom() 
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 78
                self.match(ShellGrammarParser.WHITESPACE)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return self.getTypedRuleContext(ShellGrammarParser.RedirectionContext,0)


        def argument(self):
            return self.getTypedRuleContext(ShellGrammarParser.ArgumentContext,0)


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = ShellGrammarParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.redirection()
                pass
            elif token in [1, 3, 4, 8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
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
                return self.getTypedRuleContexts(ShellGrammarParser.QuotedContext)
            else:
                return self.getTypedRuleContext(ShellGrammarParser.QuotedContext,i)


        def UNQUOTED(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.UNQUOTED)
            else:
                return self.getToken(ShellGrammarParser.UNQUOTED, i)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = ShellGrammarParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 90
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [3, 4, 8]:
                        self.state = 88
                        self.quoted()
                        pass
                    elif token in [1]:
                        self.state = 89
                        self.match(ShellGrammarParser.UNQUOTED)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 92 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
            return self.getToken(ShellGrammarParser.LESS_THAN, 0)

        def argument(self):
            return self.getTypedRuleContext(ShellGrammarParser.ArgumentContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.WHITESPACE)
            else:
                return self.getToken(ShellGrammarParser.WHITESPACE, i)

        def GREATER_THAN(self):
            return self.getToken(ShellGrammarParser.GREATER_THAN, 0)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_redirection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRedirection" ):
                listener.enterRedirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRedirection" ):
                listener.exitRedirection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRedirection" ):
                return visitor.visitRedirection(self)
            else:
                return visitor.visitChildren(self)




    def redirection(self):

        localctx = ShellGrammarParser.RedirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(ShellGrammarParser.LESS_THAN)
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 95
                    self.match(ShellGrammarParser.WHITESPACE)
                    self.state = 100
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 101
                self.argument()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(ShellGrammarParser.GREATER_THAN)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 103
                    self.match(ShellGrammarParser.WHITESPACE)
                    self.state = 108
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 109
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


    class QuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleQuoted(self):
            return self.getTypedRuleContext(ShellGrammarParser.SingleQuotedContext,0)


        def doubleQuoted(self):
            return self.getTypedRuleContext(ShellGrammarParser.DoubleQuotedContext,0)


        def backQuoted(self):
            return self.getTypedRuleContext(ShellGrammarParser.BackQuotedContext,0)


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_quoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuoted" ):
                listener.enterQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuoted" ):
                listener.exitQuoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuoted" ):
                return visitor.visitQuoted(self)
            else:
                return visitor.visitChildren(self)




    def quoted(self):

        localctx = ShellGrammarParser.QuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_quoted)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.singleQuoted()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.doubleQuoted()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
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
                return self.getTokens(ShellGrammarParser.SINGLE_QUOTE)
            else:
                return self.getToken(ShellGrammarParser.SINGLE_QUOTE, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.NEWLINE)
            else:
                return self.getToken(ShellGrammarParser.NEWLINE, i)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_singleQuoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleQuoted" ):
                listener.enterSingleQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleQuoted" ):
                listener.exitSingleQuoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleQuoted" ):
                return visitor.visitSingleQuoted(self)
            else:
                return visitor.visitChildren(self)




    def singleQuoted(self):

        localctx = ShellGrammarParser.SingleQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_singleQuoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(ShellGrammarParser.SINGLE_QUOTE)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1526) != 0):
                self.state = 118
                _la = self._input.LA(1)
                if _la <= 0 or _la==3 or _la==9:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.match(ShellGrammarParser.SINGLE_QUOTE)
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
                return self.getTokens(ShellGrammarParser.DOUBLE_QUOTE)
            else:
                return self.getToken(ShellGrammarParser.DOUBLE_QUOTE, i)

        def backQuoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellGrammarParser.BackQuotedContext)
            else:
                return self.getTypedRuleContext(ShellGrammarParser.BackQuotedContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.NEWLINE)
            else:
                return self.getToken(ShellGrammarParser.NEWLINE, i)

        def BACKQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.BACKQUOTE)
            else:
                return self.getToken(ShellGrammarParser.BACKQUOTE, i)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_doubleQuoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoubleQuoted" ):
                listener.enterDoubleQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoubleQuoted" ):
                listener.exitDoubleQuoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoubleQuoted" ):
                return visitor.visitDoubleQuoted(self)
            else:
                return visitor.visitChildren(self)




    def doubleQuoted(self):

        localctx = ShellGrammarParser.DoubleQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_doubleQuoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(ShellGrammarParser.DOUBLE_QUOTE)
            self.state = 131
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 129
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8]:
                        self.state = 127
                        self.backQuoted()
                        pass
                    elif token in [1, 2, 3, 4, 5, 6, 7, 10]:
                        self.state = 128
                        _la = self._input.LA(1)
                        if _la <= 0 or _la==8 or _la==9:
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 133
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 134
            self.match(ShellGrammarParser.DOUBLE_QUOTE)
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
                return self.getTokens(ShellGrammarParser.BACKQUOTE)
            else:
                return self.getToken(ShellGrammarParser.BACKQUOTE, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.NEWLINE)
            else:
                return self.getToken(ShellGrammarParser.NEWLINE, i)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_backQuoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBackQuoted" ):
                listener.enterBackQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBackQuoted" ):
                listener.exitBackQuoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBackQuoted" ):
                return visitor.visitBackQuoted(self)
            else:
                return visitor.visitChildren(self)




    def backQuoted(self):

        localctx = ShellGrammarParser.BackQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_backQuoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(ShellGrammarParser.BACKQUOTE)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1278) != 0):
                self.state = 137
                _la = self._input.LA(1)
                if _la <= 0 or _la==8 or _la==9:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 143
            self.match(ShellGrammarParser.BACKQUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





