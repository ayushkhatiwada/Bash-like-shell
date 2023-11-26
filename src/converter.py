from antlr.ShellGrammarParser import ShellGrammarParser
from antlr.ShellGrammarVisitor import ShellGrammarVisitor
from commands import *


class Converter(ShellGrammarVisitor):
    def __init__(self) -> None:
        super().__init__()

    def visitCommand(self, ctx: ShellGrammarParser.CommandContext):
        pass

    def visitPipe(self, ctx: ShellGrammarParser.PipeContext):
        pass

    def visitSeq(self, ctx: ShellGrammarParser.SeqContext):
        pass

    def visitCall(self, ctx: ShellGrammarParser.CallContext):
        pass
