# Generated from ShellGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ShellGrammarParser import ShellGrammarParser
else:
    from ShellGrammarParser import ShellGrammarParser


# This class defines a complete generic visitor for a parse tree produced by
# ShellGrammarParser
class ShellGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ShellGrammarParser#command.
    def visitCommand(self, ctx:ShellGrammarParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#pipe.
    def visitPipe(self, ctx:ShellGrammarParser.PipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#seq.
    def visitSeq(self, ctx:ShellGrammarParser.SeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#call.
    def visitCall(self, ctx:ShellGrammarParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#quoted.
    def visitQuoted(self, ctx:ShellGrammarParser.QuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#singleQuoted.
    def visitSingleQuoted(self, ctx:ShellGrammarParser.SingleQuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#backQuoted.
    def visitBackQuoted(self, ctx:ShellGrammarParser.BackQuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#doubleQuoted.
    def visitDoubleQuoted(self, ctx:ShellGrammarParser.DoubleQuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#atom.
    def visitAtom(self, ctx:ShellGrammarParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#argument.
    def visitArgument(self, ctx:ShellGrammarParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#redirection.
    def visitRedirection(self, ctx:ShellGrammarParser.RedirectionContext):
        return self.visitChildren(ctx)



del ShellGrammarParser