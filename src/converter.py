from antlr.ShellGrammarParser import ShellGrammarParser
from antlr.ShellGrammarVisitor import ShellGrammarVisitor

from expressions import (
    Command,
    Pipe,
    Seq,
    Call,
    Atom,
    Redirection,
    Argument,
    Quoted,
    SingleQuoted,
    DoubleQuoted,
    BackQuoted,
)

# TODO: change AssertionErrors to something more specific


# double check Pipe and Seq with HJP/XLow
class Converter(ShellGrammarVisitor):
    def __init__(self, out=None) -> None:
        super().__init__()

    def visitCommand(self, ctx: ShellGrammarParser.CommandContext):
        child = ctx.children[0]

        if isinstance(child, ShellGrammarParser.PipeContext):
            return Command(self.visitPipe(child))
        elif isinstance(child, ShellGrammarParser.SeqContext):
            return Command(self.visitSeq(child))
        elif isinstance(child, ShellGrammarParser.CallContext):
            return Command(self.visitCall(child))

        raise AssertionError("Command must be of type pipe, seq or call")

    def visitPipe(self, ctx: ShellGrammarParser.PipeContext):
        left_child = ctx.children[0]
        left_side = self.visitCall(left_child)

        right_side = ctx.children[2]
        if isinstance(right_side, ShellGrammarParser.CallContext):
            right_side = self.visitCall(right_side)
        elif isinstance(right_side, ShellGrammarParser.PipeContext):
            right_side = self.visitPipe(right_side)
        else:
            raise AssertionError(
                """
                Right side of | must be either of type pipe or call
            """
            )

        return Pipe(left_side, right_side)

    def visitSeq(self, ctx: ShellGrammarParser.SeqContext):
        left_side = ctx.children[0]
        if isinstance(left_side, ShellGrammarParser.PipeContext):
            left_side = self.visitPipe(left_side)
        elif isinstance(left_side, ShellGrammarParser.CallContext):
            left_side = self.visitCall(left_side)
        else:
            raise AssertionError(
                """Left side of ; must be either of type pipe
            or call"""
            )

        right_side = ctx.children[2]
        if isinstance(right_side, ShellGrammarParser.PipeContext):
            right_side = self.visitPipe(right_side)
        elif isinstance(right_side, ShellGrammarParser.SeqContext):
            right_side = self.visitSeq(right_side)
        elif isinstance(right_side, ShellGrammarParser.CallContext):
            right_side = self.visitCall(right_side)
        else:
            raise AssertionError(
                "Right side of ; must be either of type "
                "pipe, seq or call"
            )

        return Seq(left_side, right_side)

    # check with HJP/XLow
    def visitCall(self, ctx: ShellGrammarParser.CallContext):
        elements = []

        for child in ctx.children:
            if isinstance(child, ShellGrammarParser.RedirectionContext):
                elements.append(self.visitRedirection(child))
            elif isinstance(child, ShellGrammarParser.ArgumentContext):
                elements.append(self.visitArgument(child))
            elif isinstance(child, ShellGrammarParser.AtomContext):
                elements.append(self.visitAtom(child))

        return Call(*elements)

    def visitAtom(self, ctx: ShellGrammarParser.AtomContext):
        child = ctx.children[0]

        if isinstance(child, ShellGrammarParser.RedirectionContext):
            return Atom(self.visitRedirection(child))
        elif isinstance(child, ShellGrammarParser.ArgumentContext):
            return Atom(self.visitArgument(child))
        else:
            raise AssertionError(
                """Atom must be of type redirection
            or argument"""
            )

    # # not 100% confient in this
    # def visitRedirection(self, ctx: ShellGrammarParser.RedirectionContext):
    #     less_than_or_greater_than = ctx.children[0]
    #     argument = ctx.children[2]

    #     if less_than_or_greater_than.getText() == ">":
    #         redirection_type = ">"
    #     elif less_than_or_greater_than.getText() == "<":
    #         redirection_type = "<"
    #     else:
    #         raise AssertionError("Redirection must be either > or <")

    #     return Redirection(redirection_type, self.visitArgument(argument))

    # not 100% confient in this
    def visitRedirection(self, ctx: ShellGrammarParser.RedirectionContext):
        less_than_or_greater_than = ctx.children[0]

        if less_than_or_greater_than.getText() == ">":
            redirection_type = ">"
        elif less_than_or_greater_than.getText() == "<":
            redirection_type = "<"
        else:
            raise AssertionError("Redirection must be either > or <")

        # bit dodgy but it works
        # problem is that redirections could have a space
        # between the redirection type and the argument
        # e.g. echo hello > file.txt vs echo hello>file.txt
        for child in ctx.children:
            if isinstance(child, ShellGrammarParser.ArgumentContext):
                argument = child

        return Redirection(redirection_type, self.visitArgument(argument))

    # def visitArgument(self, ctx: ShellGrammarParser.ArgumentContext):
    #     child = ctx.children[0]

    #     if isinstance(child, ShellGrammarParser.QuotedContext):
    #         return Argument(self.visitQuoted(child))
    #     else:
    #         return Argument(child.getText())

    """
    # Alternative implementation of visitArgument
    # Because Arugment can have multiple children
    # e.g. echo "hello"'world'lol - check on ANTLR tree
    # Argument(
    #   Quoted(DoubleQuoted("hello")),
    #   Quoted(SingleQuoted('world')), lol
    # )
    """

    def visitArgument(self, ctx: ShellGrammarParser.ArgumentContext):
        elements = []

        for child in ctx.children:
            if isinstance(child, ShellGrammarParser.QuotedContext):
                elements.append(self.visitQuoted(child))
            else:
                # base case: child is text
                elements.append(child.getText())

        return Argument(*elements)

    def visitQuoted(self, ctx: ShellGrammarParser.QuotedContext):
        child = ctx.children[0]

        if isinstance(child, ShellGrammarParser.SingleQuotedContext):
            return Quoted(self.visitSingleQuoted(child))
        elif isinstance(child, ShellGrammarParser.DoubleQuotedContext):
            return Quoted(self.visitDoubleQuoted(child))
        elif isinstance(child, ShellGrammarParser.BackQuotedContext):
            return Quoted(self.visitBackQuoted(child))
        else:
            raise AssertionError(
                """Quoted must be of type singleQuoted,
            doubleQuoted or backQuoted"""
            )

    def visitSingleQuoted(self, ctx: ShellGrammarParser.SingleQuotedContext):
        elements = []
        for child in ctx.getChildren():
            if child.getText() == "'":
                continue
            elements.append(child.getText())

        return SingleQuoted(*elements)

    # From HJP/XLow - might need to change
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

    def visitBackQuoted(self, ctx: ShellGrammarParser.BackQuotedContext):
        child = ""
        for c in ctx.children:
            if c.getText() == "`":
                continue
            child += c.getText()

        return BackQuoted(child)
