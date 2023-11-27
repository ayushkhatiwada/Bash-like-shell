from antlr.ShellGrammarParser import ShellGrammarParser
from antlr.ShellGrammarVisitor import ShellGrammarVisitor

from expressions import (
    Commmand,
    Pipe,
    Seq,
    Call
)


class Converter(ShellGrammarVisitor):
    def __init__(self, out) -> None:
        super().__init__()
        # uras stuff
        # self.out = out
        # self.pipeData = None

    def visitCommand(self, ctx: ShellGrammarParser.CommandContext):
        child = ctx.children[0]

        if type(child) == ShellGrammarParser.PipeContext:
            return Pipe(child)
        elif type(child) == ShellGrammarParser.SeqContext:
            return Seq(child)
        elif type(child) == ShellGrammarParser.CallContext:
            return Call(child)
        
        raise AssertionError("Command must be of type pipe, seq or call")
    

    def visitPipe(self, ctx: ShellGrammarParser.PipeContext):
        left_side = Call(ctx.children[0])

        right_side = ctx.children[2]
        if type(right_side) == ShellGrammarParser.CallContext:
            right_side = Call(right_side)
        elif type(right_side) == ShellGrammarParser.PipeContext:
            right_side = Pipe(right_side)
        else:
            raise AssertionError("Right side of | must be either of type pipe or call")

        return Pipe(left_side, right_side)

        # uras stuff
        # for child in ctx.getChildren():
        #     self.visit(child)
        #     self.pipeData = self.out.pop()

    def visitSeq(self, ctx: ShellGrammarParser.SeqContext):
        left_side = ctx.children[0]
        if type(left_side) == ShellGrammarParser.PipeContext:
            left_side = Pipe(left_side)
        elif type(left_side)  == ShellGrammarParser.CallContext:
            left_side = Call(left_side)
        else:
            raise AssertionError("Sum ting wong with seq converter.py")

        right_side = ctx.children[2]
        if type(right_side) == ShellGrammarParser.PipeContext:
            right_side = Pipe(right_side)
        elif type(right_side) == ShellGrammarParser.SeqContext:
            right_side = Seq(right_side)
        elif type(right_side) == ShellGrammarParser.CallContext:
            right_side = Call(right_side)
        else:
            raise AssertionError("Sum ting wong with seq converter.py")

        return Seq(left_side, right_side)

    def visitCall(self, ctx: ShellGrammarParser.CallContext):
        
        
        pass
