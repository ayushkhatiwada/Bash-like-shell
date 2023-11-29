from visitor import Visitor


"""
Implementation of commands (Pipe, Seq, Call) will be done here
Each class will have an eval method that will evaluate the command
This is clear in the UML diagram from Sergey

Ignore the accept method, they will be deleted
"""


class AbstractShellFeature:
    def __init__(self) -> None:
        pass


class Commmand(AbstractShellFeature):
    def __init__(self, child) -> None:
        super().__init__()
        self.child = child

    def accept(self, visitor: Visitor):
        return visitor.visit_command(self)


class Pipe(AbstractShellFeature):
    def __init__(self, left_side, right_side) -> None:
        super().__init__()
        self.left_side = left_side
        self.right_side = right_side

    def eval(self, input, output):
        pass

    def accept(self, visitor: Visitor):
        return visitor.visit_pipe(self)


class Seq(AbstractShellFeature):

    def accept(self, visitor: Visitor):
        return visitor.visit_seq(self)


class Call(AbstractShellFeature):

    def accept(self, visitor: Visitor):
        return visitor.visit_call(self)


class Atom(AbstractShellFeature):

    def accept(self, visitor: Visitor):
        return visitor.visit_atom(self)


class Redirection(AbstractShellFeature):

    def accept(self, visitor: Visitor):
        return visitor.visit_redirection(self)


class Argument(AbstractShellFeature):

    def accept(self, visitor: Visitor):
        return visitor.visit_argument(self)


class Quoted(AbstractShellFeature):

    def accept(self, visitor: Visitor):
        return visitor.visit_quoted(self)


class SingleQuoted(AbstractShellFeature):

    def accept(self, visitor: Visitor):
        return visitor.visit_single_quoted(self)


class DoubleQuoted(AbstractShellFeature):

    def accept(self, visitor: Visitor):
        return visitor.visit_double_quoted(self)


class BackQuoted(AbstractShellFeature):

    def accept(self, visitor: Visitor):
        return visitor.visit_back_quoted(self)
