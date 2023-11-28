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

    def visit_command(self, shellfeature: Commmand) -> deque[str]:
        pass

    def visit_pipe(self: Visitor, shellfeature: Pipe) -> deque[str]:
        pass

    def visit_seq(self, shellfeature: Seq) -> deque[str]:
        pass

    def visit_call(self, shellfeature: Call) -> deque[str]:
        pass

    def visit_atom(self, shellfeature: Atom) -> deque[str]:
        pass

    def visit_redirection(self, shellfeature: Redirection) -> deque[str]:
        pass

    def visit_argument(self, shellfeature: Argument) -> deque[str]:
        pass

    def visit_quoted(self, shellfeature: Quoted) -> deque[str]:
        pass

    def visit_single_quoted(self, shellfeature: SingleQuoted) -> deque[str]:
        pass

    def visit_double_quoted(self, shellfeature: DoubleQuoted) -> deque[str]:
        pass

    def visit_back_quoted(self, shellfeature: BackQuoted) -> deque[str]:
        pass
