from antlr.ShellGrammarParser import ShellGrammarParser
from antlr.ShellGrammarVisitor import ShellGrammarVisitor
from commands import *


class Converter(ShellGrammarVisitor):
    def __init__(self, out) -> None:
        super().__init__()
        self.out = out
        self.pipeData = None

    def visitCommand(self, ctx: ShellGrammarParser.CommandContext):
        pass

    def visitPipe(self, ctx: ShellGrammarParser.PipeContext):
        for child in ctx.getChildren():
            self.visit(child)
            self.pipeData = self.out.pop()

    def visitSeq(self, ctx: ShellGrammarParser.SeqContext):
        pass

    def visitCall(self, ctx: ShellGrammarParser.CallContext):
        pass
