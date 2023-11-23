# Generated from CommandGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CommandGrammarParser import CommandGrammarParser
else:
    from CommandGrammarParser import CommandGrammarParser

# This class defines a complete generic visitor for a parse tree produced by CommandGrammarParser.

class CommandGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CommandGrammarParser#command.
    def visitCommand(self, ctx:CommandGrammarParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandGrammarParser#pipe.
    def visitPipe(self, ctx:CommandGrammarParser.PipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandGrammarParser#seq.
    def visitSeq(self, ctx:CommandGrammarParser.SeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandGrammarParser#call.
    def visitCall(self, ctx:CommandGrammarParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandGrammarParser#quoted.
    def visitQuoted(self, ctx:CommandGrammarParser.QuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandGrammarParser#singleQuoted.
    def visitSingleQuoted(self, ctx:CommandGrammarParser.SingleQuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandGrammarParser#backQuoted.
    def visitBackQuoted(self, ctx:CommandGrammarParser.BackQuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandGrammarParser#doubleQuoted.
    def visitDoubleQuoted(self, ctx:CommandGrammarParser.DoubleQuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandGrammarParser#atom.
    def visitAtom(self, ctx:CommandGrammarParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandGrammarParser#argument.
    def visitArgument(self, ctx:CommandGrammarParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandGrammarParser#redirection.
    def visitRedirection(self, ctx:CommandGrammarParser.RedirectionContext):
        return self.visitChildren(ctx)



del CommandGrammarParser