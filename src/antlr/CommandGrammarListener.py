# Generated from CommandGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CommandGrammarParser import CommandGrammarParser
else:
    from CommandGrammarParser import CommandGrammarParser

# This class defines a complete listener for a parse tree produced by CommandGrammarParser.
class CommandGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by CommandGrammarParser#command.
    def enterCommand(self, ctx:CommandGrammarParser.CommandContext):
        pass

    # Exit a parse tree produced by CommandGrammarParser#command.
    def exitCommand(self, ctx:CommandGrammarParser.CommandContext):
        pass


    # Enter a parse tree produced by CommandGrammarParser#pipe.
    def enterPipe(self, ctx:CommandGrammarParser.PipeContext):
        pass

    # Exit a parse tree produced by CommandGrammarParser#pipe.
    def exitPipe(self, ctx:CommandGrammarParser.PipeContext):
        pass


    # Enter a parse tree produced by CommandGrammarParser#seq.
    def enterSeq(self, ctx:CommandGrammarParser.SeqContext):
        pass

    # Exit a parse tree produced by CommandGrammarParser#seq.
    def exitSeq(self, ctx:CommandGrammarParser.SeqContext):
        pass


    # Enter a parse tree produced by CommandGrammarParser#call.
    def enterCall(self, ctx:CommandGrammarParser.CallContext):
        pass

    # Exit a parse tree produced by CommandGrammarParser#call.
    def exitCall(self, ctx:CommandGrammarParser.CallContext):
        pass


    # Enter a parse tree produced by CommandGrammarParser#quoted.
    def enterQuoted(self, ctx:CommandGrammarParser.QuotedContext):
        pass

    # Exit a parse tree produced by CommandGrammarParser#quoted.
    def exitQuoted(self, ctx:CommandGrammarParser.QuotedContext):
        pass


    # Enter a parse tree produced by CommandGrammarParser#singleQuoted.
    def enterSingleQuoted(self, ctx:CommandGrammarParser.SingleQuotedContext):
        pass

    # Exit a parse tree produced by CommandGrammarParser#singleQuoted.
    def exitSingleQuoted(self, ctx:CommandGrammarParser.SingleQuotedContext):
        pass


    # Enter a parse tree produced by CommandGrammarParser#backQuoted.
    def enterBackQuoted(self, ctx:CommandGrammarParser.BackQuotedContext):
        pass

    # Exit a parse tree produced by CommandGrammarParser#backQuoted.
    def exitBackQuoted(self, ctx:CommandGrammarParser.BackQuotedContext):
        pass


    # Enter a parse tree produced by CommandGrammarParser#doubleQuoted.
    def enterDoubleQuoted(self, ctx:CommandGrammarParser.DoubleQuotedContext):
        pass

    # Exit a parse tree produced by CommandGrammarParser#doubleQuoted.
    def exitDoubleQuoted(self, ctx:CommandGrammarParser.DoubleQuotedContext):
        pass


    # Enter a parse tree produced by CommandGrammarParser#atom.
    def enterAtom(self, ctx:CommandGrammarParser.AtomContext):
        pass

    # Exit a parse tree produced by CommandGrammarParser#atom.
    def exitAtom(self, ctx:CommandGrammarParser.AtomContext):
        pass


    # Enter a parse tree produced by CommandGrammarParser#argument.
    def enterArgument(self, ctx:CommandGrammarParser.ArgumentContext):
        pass

    # Exit a parse tree produced by CommandGrammarParser#argument.
    def exitArgument(self, ctx:CommandGrammarParser.ArgumentContext):
        pass


    # Enter a parse tree produced by CommandGrammarParser#redirection.
    def enterRedirection(self, ctx:CommandGrammarParser.RedirectionContext):
        pass

    # Exit a parse tree produced by CommandGrammarParser#redirection.
    def exitRedirection(self, ctx:CommandGrammarParser.RedirectionContext):
        pass



del CommandGrammarParser