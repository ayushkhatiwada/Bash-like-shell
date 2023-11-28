from antlr.ShellGrammarParser import ShellGrammarParser
from antlr.ShellGrammarVisitor import ShellGrammarVisitor

from expressions import (
    Commmand,
    Pipe,
    Seq,
    Call,
    Atom,
    Argument,
    Redirection,
    Quoted,
    SingleQuoted,
    BackQuoted,
    DoubleQuoted
)

# double check Pipe and Seq with HJP/XLow

class Converter(ShellGrammarVisitor):
    def __init__(self, out) -> None:
        super().__init__()

    def visitCommand(self, ctx: ShellGrammarParser.CommandContext):
        child = ctx.children[0]

        if type(child) == ShellGrammarParser.PipeContext:
            return Commmand(self.visitPipe(child))
        elif type(child) == ShellGrammarParser.SeqContext:
            return Commmand(self.visitSeq(child))
        elif type(child) == ShellGrammarParser.CallContext:
            return Commmand(self.visitCall(child))
        
        raise AssertionError("Command must be of type pipe, seq or call")

    def visitPipe(self, ctx: ShellGrammarParser.PipeContext):
        left_child = ctx.children[0]
        left_side = self.visitCall(left_child)

        right_side = ctx.children[2]
        if type(right_side) == ShellGrammarParser.CallContext:
            right_side = self.visitCall(right_side)
        elif type(right_side) == ShellGrammarParser.PipeContext:
            right_side = self.visitPipe(right_side)
        else:
            raise AssertionError("Right side of | must be either of type pipe or call")

        return Pipe(left_side, right_side)

    def visitSeq(self, ctx: ShellGrammarParser.SeqContext):
        left_side = ctx.children[0]
        if type(left_side) == ShellGrammarParser.PipeContext:
            left_side = self.visitPipe(left_side)
        elif type(left_side)  == ShellGrammarParser.CallContext:
            left_side = self.visitCall(left_side)
        else:
            raise AssertionError("Left side of ; must be either of type pipe or call")

        right_side = ctx.children[2]
        if type(right_side) == ShellGrammarParser.PipeContext:
            right_side = self.visitPipe(right_side)
        elif type(right_side) == ShellGrammarParser.SeqContext:
            right_side = self.visitSeq(right_side)
        elif type(right_side) == ShellGrammarParser.CallContext:
            right_side = self.visitCall(right_side)
        else:
            raise AssertionError("Right side of ; must be either of type pipe, seq or call")

        return Seq(left_side, right_side)

    def visitCall(self, ctx: ShellGrammarParser.CallContext):
        elements = []

        for child in ctx.children:
            if type(child) == ShellGrammarParser.RedirectionContext:
                child = Redirection(self.visitRedirection(child))
                elements.append(child)
            elif type(child) == ShellGrammarParser.ArgumentContext:
                child = Argument(self.visitArgument(child))
                elements.append(child)
            elif type(child) == ShellGrammarParser.AtomContext:
                child = Atom(self.visitAtom(child))
                elements.append(child)
            else:
                pass

        return Call(*elements)

    def visitAtom(self, ctx: ShellGrammarParser.AtomContext):
        child = ctx.children[0]

        if type(child) == ShellGrammarParser.RedirectionContext:
            return Atom(self.visitRedirection(child))
        elif type(child) == ShellGrammarParser.ArgumentContext:
            return Atom(self.visitArgument(child))
        else:
            raise AssertionError("Atom must be of type redirection or argument")

    def visitArgument(self, ctx: ShellGrammarParser.ArgumentContext):
        child = ctx.children[0]

        if type(child) == ShellGrammarParser.QuotedContext:
            return Argument(self.visitQuoted(child))
        else:
            return child.getText()

    # not 100% confient in this
    def visitRedirection(self, ctx: ShellGrammarParser.RedirectionContext):
        less_than_or_greater_than = ctx.children[0]
        argument = ctx.children[2]


    def visitQuoted(self, ctx: ShellGrammarParser.QuotedContext):
        child = ctx.children[0]

        if type(child) == ShellGrammarParser.SingleQuotedContext:
            return Quoted(self.visitSingleQuoted(child))
        elif type(child) == ShellGrammarParser.DoubleQuotedContext:
            return Quoted(self.visitDoubleQuoted(child))
        elif type(child) == ShellGrammarParser.BackQuotedContext:
            return Quoted(self.visitBackQuoted(child))
        else:
            raise AssertionError("Quoted must be of type singleQuoted, doubleQuoted or backQuoted")

    def visitSingleQuoted(self, ctx: ShellGrammarParser.SingleQuotedContext):
        child = ctx.children[0]
        # [1:-1] removes the single quotes from the string
        return SingleQuoted(child.getText()[1:-1])

    def visitBackQuoted(self, ctx: ShellGrammarParser.BackQuotedContext):
        child = ctx.children[0]
        return BackQuoted(child.getText()[1:-1])
    
    # Code from HJP/XLow
    def visitDoubleQuoted(self, ctx: ShellGrammarParser.DoubleQuotedContext):
        elements = []
        curr = ""

        for child in ctx.getChildren():
            if isinstance(child, ShellGrammarParser.BackQuotedContext):
                if curr:
                    elements.append(curr)
                    curr = ""
                elements.append(self.visitBackQuoted(child))

            else:
                # Skip "" in converter formatting
                if child.getText() == '"':
                    continue
                curr += child.getText()

        if curr:
            elements.append(curr)

        return DoubleQuoted(*elements)
