"""
Implementation of commands (Pipe, Seq, Call) will be done here
Each class will have an eval method that will evaluate the command
This is clear in the UML diagram from Sergey

Ignore the accept method, they will be deleted
"""


class AbstractShellFeature:
    def __init__(self, child) -> None:
        self.child = child


class Commmand(AbstractShellFeature):
    def __init__(self, child) -> None:
        super().__init__(child)

    def eval(self, input, output):
        pass


class Pipe(AbstractShellFeature):
    def __init__(self, left_side=None, right_side=None) -> None:
        self.left_side = left_side
        self.right_side = right_side

    def eval(self, input, output):
        pass


class Seq(AbstractShellFeature):
    def __init__(self, child) -> None:
        super().__init__(child)

    def eval(self, input, output):
        pass


class Call(AbstractShellFeature):
    def __init__(self, child) -> None:
        super().__init__(child)

    def eval(self, input, output):
        pass


class Atom(AbstractShellFeature):
    def __init__(self, child) -> None:
        super().__init__(child)

    def eval(self, input, output):
        pass


class Redirection(AbstractShellFeature):
    def __init__(self, child) -> None:
        super().__init__(child)

    def eval(self, input, output):
        pass


class Argument(AbstractShellFeature):
    def __init__(self, child) -> None:
        super().__init__(child)

    def eval(self, input, output):
        pass


class Quoted(AbstractShellFeature):
    def __init__(self, child) -> None:
        super().__init__(child)

    def eval(self, input, output):
        pass


class SingleQuoted(AbstractShellFeature):
    def __init__(self, child) -> None:
        super().__init__(child)

    def eval(self, input, output):
        pass


class DoubleQuoted(AbstractShellFeature):
    def __init__(self, child) -> None:
        super().__init__(child)

    def eval(self, input, output):
        pass


class BackQuoted(AbstractShellFeature):
    def __init__(self, child) -> None:
        super().__init__(child)

    def eval(self, input, output):
        pass
