# Generated from CommandGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,11,51,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,1,2,1,2,
        1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,4,8,41,8,8,11,8,12,8,
        42,1,9,1,9,1,10,4,10,48,8,10,11,10,12,10,49,0,0,11,1,1,3,2,5,3,7,
        4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,1,0,3,3,0,9,9,13,13,32,32,
        6,0,10,10,34,34,39,39,59,59,96,96,124,124,8,0,9,10,32,32,34,34,39,
        39,59,60,62,62,96,96,124,124,52,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,
        0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,
        0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,23,1,0,0,0,3,25,1,0,0,
        0,5,27,1,0,0,0,7,29,1,0,0,0,9,31,1,0,0,0,11,33,1,0,0,0,13,35,1,0,
        0,0,15,37,1,0,0,0,17,40,1,0,0,0,19,44,1,0,0,0,21,47,1,0,0,0,23,24,
        5,124,0,0,24,2,1,0,0,0,25,26,5,39,0,0,26,4,1,0,0,0,27,28,5,34,0,
        0,28,6,1,0,0,0,29,30,5,59,0,0,30,8,1,0,0,0,31,32,5,60,0,0,32,10,
        1,0,0,0,33,34,5,62,0,0,34,12,1,0,0,0,35,36,5,96,0,0,36,14,1,0,0,
        0,37,38,5,10,0,0,38,16,1,0,0,0,39,41,7,0,0,0,40,39,1,0,0,0,41,42,
        1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,18,1,0,0,0,44,45,8,1,0,0,
        45,20,1,0,0,0,46,48,8,2,0,0,47,46,1,0,0,0,48,49,1,0,0,0,49,47,1,
        0,0,0,49,50,1,0,0,0,50,22,1,0,0,0,3,0,42,49,0
    ]

class CommandGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PIPE = 1
    SINGLE_QUOTE = 2
    DOUBLE_QUOTE = 3
    SEMI_COLON = 4
    LESS_THAN = 5
    GREATER_THAN = 6
    BACKQUOTE = 7
    NEWLINE = 8
    WHITESPACE = 9
    NON_KEYWORD = 10
    UNQUOTED = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'|'", "'''", "'\"'", "';'", "'<'", "'>'", "'`'", "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "PIPE", "SINGLE_QUOTE", "DOUBLE_QUOTE", "SEMI_COLON", "LESS_THAN", 
            "GREATER_THAN", "BACKQUOTE", "NEWLINE", "WHITESPACE", "NON_KEYWORD", 
            "UNQUOTED" ]

    ruleNames = [ "PIPE", "SINGLE_QUOTE", "DOUBLE_QUOTE", "SEMI_COLON", 
                  "LESS_THAN", "GREATER_THAN", "BACKQUOTE", "NEWLINE", "WHITESPACE", 
                  "NON_KEYWORD", "UNQUOTED" ]

    grammarFileName = "CommandGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


