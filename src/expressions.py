from typing import Deque
from abc import ABC, abstractmethod

import shell
from application_factory import ApplicationFactory

"""
Implementation of commands (Pipe, Seq, Call) will be done here
Each class will have an eval method that will evaluate the command
This is clear in the UML diagram from Sergey
"""
"""
echo hello
Command(Call(Argument(echo), Atom(Argument(hello)))).eval()
"""


class AbstractShellFeature(ABC):
    def __str__(self):
        return "AbstractShellFeature"

    def __eq__(self, other):
        pass

    @abstractmethod
    def eval(self, input, output):
        pass


class Commmand(AbstractShellFeature):
    def __init__(self, child):
        self.child = child

    def __str__(self):
        return f"Commmand({self.child})"

    def __eq__(self, other):
        return isinstance(other, Commmand) and self.child == other.child

    def eval(self, input: Deque[str] = None, output: Deque[str] = None):
        # return self.child.eval(input, output)

        # Don't need to return anything in eval
        # Because output is a deque that is passed around
        self.child.eval(input, output)


##############################################################################
# dunno if this works
class Pipe(AbstractShellFeature):
    def __init__(self, left, right) -> None:
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
        # self.args is a tuple
        # it contains redirection, argument, or atom classes
        self.args = args

    def __str__(self):
        args_str = ", ".join(str(arg) for arg in self.args)
        return f"Call({args_str})"

    def __eq__(self, other):
        return isinstance(other, Call) and self.args == other.args

    def eval(self, input, output):
        # self.args could be (Redirection(), Argument(), Atom(), Atom(), ...)
        # eval each class in self.args and store in new_args list
        new_args = [c.eval(input, output) for c in self.args]
        # now I have a bunch of shit to deal with

        # attempt 1: which handles a simple case
        application_name = new_args[0]
        args = new_args[1:]

        app = ApplicationFactory().get_application([application_name])
        app.exec(args, None, output)


class Atom(AbstractShellFeature):
    def __init__(self, child):
        self.child = child

    def __str__(self):
        return f"Atom({self.child})"

    def __eq__(self, other):
        return isinstance(other, Atom) and self.child == other.child

    def eval(self, input, output):
        # Atoms' children are either redirection or argument
        return self.child.eval(input, output)


###############################################################################
class Redirection(AbstractShellFeature):
    """
    Redirection from Sergey's README:
    1. Opens the file following the < symbol for input redirection;
    2. Opens the file following the > symbol for output redirection;
    3. If several files are specified for input or output redirection
        - (e.g. > a.txt > b.txt), throws an exception;
    4. If the file specified for input redirection does not exist,
        - throws an exception;
    5. If the file specified for output redirection does not exist, creates it.

    So >> is not needed
    """

    def __init__(self, type, argument_class):
        # redirection has two children
        # left child is redirection type (> or <)
        # right child is an argument class
        # check antlr tree to see what I mean
        self.type = type
        self.argument_class = argument_class

    def __str__(self):
        return f"Redirection({self.type}, {self.file})"

    def __eq__(self, other):
        return (
            isinstance(other, Redirection)
            and self.type == other.type
            and self.file == other.file
        )

    def eval(self, input, output):
        # eval argument class (right child)
        argument = self.argument_class.eval(input, output)
        return (self.type, argument)


class Argument(AbstractShellFeature):
    def __init__(self, child):
        self.child = child

    def __str__(self):
        return f"Argument({self.child})"

    def __eq__(self, other):
        return isinstance(other, Argument) and self.child == other.child

    # child of argument could be Quoted class or text (e.g. "echo")
    def eval(self, input, output):
        # child is quoted class
        if isinstance(self.child, Quoted):
            return self.child.eval(input, output)
        # child is text
        else:
            return self.child


class Quoted(AbstractShellFeature):
    def __init__(self, child):
        self.child = child

    def __str__(self):
        return f"Quoted({self.child})"

    def __eq__(self, other):
        return isinstance(other, Quoted) and self.child == other.child

    def eval(self, input, output):
        # Quoted's child is either single quoted, double quoted, or back quoted
        return self.child.eval(input, output)


class SingleQuoted(AbstractShellFeature):
    def __init__(self, child):
        self.child = child

    def __str__(self):
        return f"SingleQuoted({self.child})"

    def __eq__(self, other):
        return isinstance(other, SingleQuoted) and self.child == other.child

    def eval(self, input, output):
        # "Base case", single quoted contains text only
        return self.child


class DoubleQuoted(AbstractShellFeature):
    # child is a list of elements
    # elements could be text or backQuoted
    # see visitDoubleQuoted method in converter.py
    # e.g. elements = [text, text, backQuoted(), text, backQuoted(), text]
    def __init__(self, child):
        self.child = child

    def __str__(self):
        return f"DoubleQuoted({self.child})"

    def __eq__(self, other):
        return isinstance(other, DoubleQuoted) and self.child == other.child

    def eval(self, input, output):
        elements = [
            c.eval() if isinstance(c, BackQuoted) else c for c in self.child
        ]
        return elements


##############################################################################
# This is quite hard to implement - AK
class BackQuoted(AbstractShellFeature):
    def __init__(self, child):
        self.child = child

    def __str__(self):
        return f"BackQuoted({self.child})"

    def __eq__(self, other):
        return isinstance(other, BackQuoted) and self.child == other.child

    # backQuoted is a sort of base case
    # it does not contain any classes inside it
    def eval(self, input, output):
        # This is black magic
        # Circular import is somehow avoided
        expression = shell.convert(self.child)
        return expression.eval()
