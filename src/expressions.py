from typing import Deque
from abc import ABC, abstractmethod
from collections import deque

import shell
from application_factory import ApplicationFactory
from applications.application import ApplicationError

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

        # std_out_left_side = self.left.eval(output)
        # self.right.eval(std_out_left_side, output)


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
        # self.args is a tuple
        # it contains redirection, argument, or atom classes
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
                    # TODO: Change this to custom exception
                    raise ApplicationError("Multiple input redirections")
                redirection_input = True

                with open(redirection.argument, "r") as file:
                    for line in file:
                        input.append(line[:-1])  # remove \n

            elif redirection.type == ">":
                if redirection_output:
                    # TODO: Change this to custom exception
                    raise ApplicationError("Multiple output redirections")
                redirection_output = True

                output_file = redirection.argument

        return input, output_file

    def eval(self, output, input=deque()):
        # self.args could be (Redirection(), Argument(), Atom(), Atom(), ...)
        # eval each class in self.args and store in evaluated_args list
        app_input = []
        while input:
            app_input.append(input.popleft()[:-1])  # remove \n

        # filter arguments and redirections
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


# Edge case: Argument can have more than one child
# e.g. echo "hello"'world'lol - check on ANTLR tree
# Argument(Quoted(DoubleQuoted("hello")), Quoted(SingleQuoted('world')), lol)
class Argument(AbstractShellFeature):
    # children is a list of elements
    # arguement can have multiple children
    def __init__(self, *children):
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
        # base case: single quoted contains text only
        result = ""
        for child in self.children:
            result += child
        return result


class DoubleQuoted(AbstractShellFeature):
    # children is a list of elements
    # elements could be text or backQuoted
    # see visitDoubleQuoted method in converter.py
    # e.g. elements = [text, text, backQuoted(), text, backQuoted(), text]
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

    # backQuoted is a sort of base case
    # it does not contain any classes inside it
    def eval(self):
        expression = shell.convert(self.child)

        expression_output = deque()
        expression.eval(expression_output)

        result = ""
        while expression_output:
            result += expression_output.popleft()  # remove \n
        return result[:-1]
