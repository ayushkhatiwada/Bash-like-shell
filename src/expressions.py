from visitor import Visitor


class AbstractCommand:
    def __init__(self) -> None:
        pass


class Commmand(AbstractCommand):

    def accept(self, visitor: Visitor):
        return visitor.visit_command(self)


class Pipe(AbstractCommand):

    def accept(self, visitor: Visitor):
        return visitor.visit_pipe(self)


class Seq(AbstractCommand):

    def accept(self, visitor: Visitor):
        return visitor.visit_seq(self)


class Call(AbstractCommand):

    def accept(self, visitor: Visitor):
        return visitor.visit_call(self)


class Atom:

    def accept(self, visitor: Visitor):
        return visitor.visit_atom(self)


class Argument:

    def accept(self, visitor: Visitor):
        return visitor.visit_argument(self)


class Redirection:

    def accept(self, visitor: Visitor):
        return visitor.visit_redirection(self)


class Quoted:

    def accept(self, visitor: Visitor):
        return visitor.visit_quoted(self)


class SingleQuoted:

    def accept(self, visitor: Visitor):
        return visitor.visit_single_quoted(self)


class BackQuoted:

    def accept(self, visitor: Visitor):
        return visitor.visit_back_quoted(self)


class DoubleQuoted:

    def accept(self, visitor: Visitor):
        return visitor.visit_double_quoted(self)
