from collections import deque

# from antlr4 import CommonTokenStream, InputStream

# from antlr.ShellGrammarLexer import ShellGrammarLexer
# from antlr.ShellGrammarParser import ShellGrammarParser
# from converter import Converter

"""
Implementation of commands (Pipe, Seq, Call) will be done here
Each class will have an eval method that will evaluate the command
This is clear in the UML diagram from Sergey
"""


class AbstractShellFeature:
    def __init__(self) -> None:
        pass

    def __str__(self):
        return "AbstractShellFeature"

    def __eq__(self, other):
        pass


class Commmand(AbstractShellFeature):
    def __init__(self, child):
        super().__init__()
        self.child = child

    def __str__(self):
        return f"Commmand({self.child})"

    def __eq__(self, other):
        return isinstance(other, Commmand) and self.child == other.child

    def eval(self, input: deque[str] = None, output: deque[str] = None):
        # ??? - check with UZK
        # return self.child.eval(input, output)

        # Don't need to return anything in eval
        # Because output is a deque that is passed around
        self.child.eval(input, output)


##############################################################################
# dunno if this works
class Pipe:
    def __init__(self, left, right) -> None:
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self):
        return f"Pipe({self.left}, {self.right})"

    def __eq__(self, other):
        return (
            isinstance(other, Pipe)
            and self.left == other.left
            and self.right == other.right
        )

    # don't need input=None, output=None
    # Because Command class's eval method has input=None, output=None
    # This input and output from Command will be passed to Pipe's eval method
    # So, Pipe's eval method will get input and output passed in
    # Same goes for Seq and Call and other nested classes
    def eval(self, input, output):
        std_out_left_side = self.left.eval(input, output)
        self.right.eval(std_out_left_side, output)


class Seq:
    def __init__(self, left, right) -> None:
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self):
        return f"Seq({self.left}, {self.right})"

    def __eq__(self, other):
        return (
            isinstance(other, Seq)
            and self.left == other.left
            and self.right == other.right
        )

    def eval(self, input, output):
        self.left.eval(input, output)
        self.right.eval(input, output)


###############################################################################
class Call(AbstractShellFeature):
    def __init__(self, *args):
        super().__init__()
        self.args = args

    def __str__(self):
        args_str = ", ".join(str(arg) for arg in self.args)
        return f"Call({args_str})"

    def __eq__(self, other):
        return isinstance(other, Call) and self.args == other.args

    def eval(self, input, output):
        pass


class Atom(AbstractShellFeature):
    def __init__(self, child):
        super().__init__()
        self.child = child

    def __str__(self):
        return f"Atom({self.child})"

    def __eq__(self, other):
        return isinstance(other, Atom) and self.child == other.child

    def eval(self, input, output):
        return self.child.eval(input, output)


###############################################################################
class Redirection(AbstractShellFeature):
    def __init__(self, type, target):
        super().__init__()
        self.type = type
        self.target = target

    def __str__(self):
        return f"Redirection({self.type}, {self.target})"

    def __eq__(self, other):
        return (
            isinstance(other, Redirection)
            and self.type == other.type
            and self.target == other.target
        )

    def eval(self, input, output):
        pass


class Argument(AbstractShellFeature):
    def __init__(self, child):
        super().__init__()
        self.child = child

    def __str__(self):
        return f"Argument({self.child})"

    def __eq__(self, other):
        return isinstance(other, Argument) and self.child == other.child

    def accept(self, visitor):
        visitor.visit_argument(self)

    # child of argument could be Quoted class or text (e.g. "echo")
    def eval(self, input, output):
        # child is quoted class
        if isinstance(self.child, Quoted):
            self.child.eval(input, output)
        # child is text
        else:
            return self.child


class Quoted(AbstractShellFeature):
    def __init__(self, child):
        super().__init__()
        self.child = child

    def __str__(self):
        return f"Quoted({self.child})"

    def __eq__(self, other):
        return isinstance(other, Quoted) and self.child == other.child

    def eval(self, input, output):
        return self.child.eval(input, output)


class SingleQuoted(AbstractShellFeature):
    def __init__(self, child):
        super().__init__()
        self.child = child

    def __str__(self):
        return f"SingleQuoted({self.child})"

    def __eq__(self, other):
        return isinstance(other, SingleQuoted) and self.child == other.child

    def eval(self, input, output):
        return self.child


class DoubleQuoted(AbstractShellFeature):
    # child is a list of elements
    # see visitDoubleQuoted method in converter.py
    # e.g. elements = [text, text, backQuoted(), text, backQuoted(), text]
    # text is double quoted content, and backQuoted() is back quoted content
    def __init__(self, child):
        super().__init__()
        self.child = child

    def __str__(self):
        return f"DoubleQuoted({self.child})"

    def __eq__(self, other):
        return isinstance(other, DoubleQuoted) and self.child == other.child

    def eval(self, input, output):
        elements = [c.eval() if isinstance(c, BackQuoted) else c for c in self.child]
        return elements


##############################################################################
class BackQuoted(AbstractShellFeature):
    def __init__(self, child):
        super().__init__()
        self.child = child

    def __str__(self):
        return f"BackQuoted({self.child})"

    def __eq__(self, other):
        return isinstance(other, BackQuoted) and self.child == other.child

    def eval(self, input, output):
        return

        # Dunno how to resolve circular import
        # cmd_line = self.child
        # std_out = deque()

        # lexer = ShellGrammarLexer(InputStream(cmd_line))
        # tokens = CommonTokenStream(lexer)
        # parser = ShellGrammarParser(tokens)

        # tree = parser.command()
        # expression = tree.accept(Converter())
        # expression.eval(output=std_out)

        # return std_out
