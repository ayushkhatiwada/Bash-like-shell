"""
This is not needed - Sergey
Implementation of commands will be done in expressions.py
Each class will have an eval method that will evaluate the command
This is clear in the UML diagram from Sergey
"""


from visitor import Visitor
from collections import deque

from expressions import (
    Commmand,
    Pipe,
    Seq,
    Call,
    Atom,
    Redirection,
    Argument,
    Quoted,
    SingleQuoted,
    DoubleQuoted,
    BackQuoted
)


class Evaluator(Visitor):
    def __init__(self) -> None:
        super().__init__()

    def visit_command(self: Visitor, command: Commmand) -> deque[str]:
        return command.child.accept(self)

    def visit_pipe(self, pipe: Pipe) -> deque[str]:
        std_out_left_side = pipe.left_side.accept(self)
        return pipe.right_side.accept(self, std_out_left_side)

    def visit_seq(self, seq: Seq) -> deque[str]:
        pass

    def visit_call(self, call: Call) -> deque[str]:
        pass

    def visit_atom(self, atom: Atom) -> deque[str]:
        pass

    def visit_redirection(self, redirection: Redirection) -> deque[str]:
        pass

    def visit_argument(self, argument: Argument) -> deque[str]:
        pass

    def visit_quoted(self, quoted: Quoted) -> deque[str]:
        pass

    def visit_single_quoted(self, singleQuoted: SingleQuoted) -> deque[str]:
        pass

    def visit_double_quoted(self, doubleQuoted: DoubleQuoted) -> deque[str]:
        pass

    def visit_back_quoted(self, backQuoted: BackQuoted) -> deque[str]:
        pass
