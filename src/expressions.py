"""
Shell Commands Implementation

This module defines classes representing various shell commands and features.
Each class corresponds to a specific command or feature in the shell.

Classes representing shell commands:
- Command
- Pipe
- Seq
- Call
- Atom
- Redirection
- Argument
- Quoted
- SingleQuoted
- DoubleQuoted
- BackQuoted

These classes are used to build and execute shell commands
within the provided shell implementation.
"""

from typing import Deque
from abc import ABC, abstractmethod
from collections import deque

import shell
from application_factory import ApplicationFactory
from applications.application import ApplicationError


class AbstractShellFeature(ABC):
    """
    Abstract base class for shell features.
    """

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def eval(self):
        pass


class Command(AbstractShellFeature):
    def __init__(self, child):
        self.child = child

    def __str__(self):
        return f"Command({self.child})"

    def __eq__(self, other):
        return isinstance(other, Command) and self.child == other.child

    def eval(self, output: Deque[str]):
        self.child.eval(output)


class Pipe(AbstractShellFeature):
    def __init__(self, left, right):
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

    def eval(self, output, input=deque()):
        left_output = deque()
        self.left.eval(left_output, input)
        self.right.eval(output, input=left_output)


class Seq:
    def __init__(self, left, right):
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

    def eval(self, output):
        self.left.eval(output)
        self.right.eval(output)


class Call(AbstractShellFeature):
    def __init__(self, *args):
        # tuple of redirections, arguments, or atom classes
        self.args = args

    def __str__(self):
        args_str = ", ".join(str(arg) for arg in self.args)
        return f"Call({args_str})"

    def __eq__(self, other):
        return isinstance(other, Call) and self.args == other.args

    def handle_redirections(self, redirections):
        input = []
        output_file = None

        redirection_input = False
        redirection_output = False

        for redirection in redirections:
            if redirection.type == "<":
                if redirection_input:
                    raise ApplicationError("Multiple input redirections")
                redirection_input = True

                with open(redirection.argument, "r") as file:
                    for line in file:
                        input.append(line[:-1])  # remove \n

            elif redirection.type == ">":
                if redirection_output:
                    raise ApplicationError("Multiple output redirections")
                redirection_output = True

                output_file = redirection.argument

        return input, output_file

    def eval(self, output, input=deque()):
        app_input = []
        while input:
            app_input.append(input.popleft()[:-1])  # remove \n

        # evaluate arguments and filter out redirections
        evaluated_args = []
        redirections = []

        for arg in self.args:
            evaluated_arg = arg.eval()

            if isinstance(evaluated_arg, Redirection):
                redirections.append(evaluated_arg)
            else:
                evaluated_args.append(evaluated_arg)

        # handle redirections
        extra_app_input, output_file = self.handle_redirections(redirections)
        app_input += extra_app_input

        application_name = evaluated_args[0]
        args = evaluated_args[1:]

        app = ApplicationFactory().get_application(application_name)

        if output_file:
            # output redirection to a file
            output_to_file = deque()
            app.exec(args, app_input, output_to_file)

            with open(output_file, "w") as file:
                while output_to_file:
                    file.write(output_to_file.popleft())
        else:
            # output to stdout
            app.exec(args, app_input, output)


class Atom(AbstractShellFeature):
    def __init__(self, child):
        self.child = child

    def __str__(self):
        return f"Atom({self.child})"

    def __eq__(self, other):
        return isinstance(other, Atom) and self.child == other.child

    def eval(self):
        # Atoms' child: redirection or argument
        return self.child.eval()


class Redirection(AbstractShellFeature):
    def __init__(self, type, argument):
        self.type: str = type  # redirection type: < or >
        self.argument: Argument = argument  # redirection arg

    def __str__(self):
        return f"Redirection({self.type}, {self.argument})"

    def __eq__(self, other):
        return (
            isinstance(other, Redirection)
            and self.type == other.type
            and self.argument == other.argument
        )

    def eval(self):
        self.argument = self.argument.eval()
        return self


class Argument(AbstractShellFeature):
    def __init__(self, *children):
        # can have multiple children
        self.children = list(children)

    def __str__(self):
        return f"Argument({[str(child) for child in self.children]})"

    def __eq__(self, other):
        return isinstance(other, Argument) and self.children == other.children

    # child of argument could be Quoted class or text (e.g. "echo")
    def eval(self) -> str:
        result = ""
        for child in self.children:
            if isinstance(child, Quoted):
                result += child.eval()
            else:
                result += child
        return result


class Quoted(AbstractShellFeature):
    def __init__(self, child):
        self.child = child

    def __str__(self):
        return f"Quoted({self.child})"

    def __eq__(self, other):
        return isinstance(other, Quoted) and self.child == other.child

    def eval(self):
        # Quoted's child: single quoted or double quoted or back quoted
        return self.child.eval()


class SingleQuoted(AbstractShellFeature):
    def __init__(self, *children):
        self.children = list(children)

    def __str__(self):
        return f"SingleQuoted({self.children})"

    def __eq__(self, other):
        return (
            isinstance(other, SingleQuoted) and self.children == other.children
        )

    def eval(self) -> str:
        result = ""
        for child in self.children:
            result += child
        return result


class DoubleQuoted(AbstractShellFeature):
    # children is a list of elements
    # elements could be text or backQuoted
    def __init__(self, *children):
        self.children = list(children)

    def __str__(self):
        return f"DoubleQuoted({self.children})"

    def __eq__(self, other):
        return (
            isinstance(other, DoubleQuoted) and
            self.children == other.children
        )

    def eval(self) -> str:
        result = ""
        for child in self.children:
            if isinstance(child, str):
                result += child
            else:
                result += child.eval()
        return result


class BackQuoted(AbstractShellFeature):
    def __init__(self, child):
        self.child = child

    def __str__(self):
        return f"BackQuoted({self.child})"

    def __eq__(self, other):
        return isinstance(other, BackQuoted) and self.child == other.child

    def eval(self):
        expression = shell.convert(self.child)

        expression_output = deque()
        expression.eval(expression_output)

        result = ""
        while expression_output:
            result += expression_output.popleft()  # remove \n
        return result[:-1]
