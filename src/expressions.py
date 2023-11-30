"""
Implementation of commands (Pipe, Seq, Call) will be done here
Each class will have an eval method that will evaluate the command
This is clear in the UML diagram from Sergey

Ignore the accept method, they will be deleted
"""

class AbstractShellFeature:
    def __init__(self, child) -> None:
        self.child = child

    def __str__(self):
        return "AbstractShellFeature"

    def __eq__(self, other):
        return isinstance(other, type(self))

class Commmand(AbstractShellFeature):
    def __init__(self, input):
        super().__init__()
        self.input = input

    def __str__(self):
        return f"Commmand(input={self.input})"

    def __eq__(self, other):
        return isinstance(other, Commmand) and self.input == other.input

    def eval(self, input, output):
        pass

class Pipe(AbstractShellFeature):
    def __init__(self, left=None, right=None) -> None:
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self):
        return f"Pipe(left={self.left}, right={self.right})"

    def __eq__(self, other):
        return isinstance(other, Pipe) and self.left == other.left and self.right == other.right

    def eval(self, input, output):
        pass

class Seq(AbstractShellFeature):
    def __init__(self, left=None, right=None) -> None:
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self):
        return f"Seq(left={self.left}, right={self.right})"

    def __eq__(self, other):
        return isinstance(other, Seq) and self.left == other.left and self.right == other.right

    def eval(self, input, output):
        pass

class Call(AbstractShellFeature):
    def __init__(self, *args):
        super().__init__()
        self.args = args

    def __str__(self):
        args_str = ', '.join(str(arg) for arg in self.args)
        return f"Call(args={args_str})"

    def __eq__(self, other):
        return isinstance(other, Call) and self.args == other.args

    def eval(self, input, output):
        pass

    
class Atom(AbstractShellFeature):
    def __init__(self, input):
        super().__init__()
        self.input = input

    def __str__(self):
        return f"Atom(input={self.input})"

    def __eq__(self, other):
        return isinstance(other, Atom) and self.input == other.input

    def eval(self, input, output):
        pass

      
class Redirection(AbstractShellFeature):
    def __init__(self, type=None, target=None):
        super().__init__()
        self.type = type
        self.target = target

    def __str__(self):
        return f"Redirection(type={self.type}, target={self.target})"

    def __eq__(self, other):
        return isinstance(other, Redirection) and self.type == other.type and self.target == other.target

    def eval(self, input, output):
        pass

class Argument(AbstractShellFeature):
    def __init__(self, input):
        super().__init__()
        self.input = input

    def __str__(self):
        return f"Argument(input={self.input})"

    def __eq__(self, other):
        return isinstance(other, Argument) and self.input == other.input

    def eval(self, input, output):
        pass

class Quoted(AbstractShellFeature):
    def __init__(self, content=None):
        super().__init__()
        self.content = content

    def __str__(self):
        return f"Quoted(content={self.content})"

    def __eq__(self, other):
        return isinstance(other, Quoted) and self.content == other.content

    def eval(self, input, output):
        pass

class SingleQuoted(AbstractShellFeature):
    def __init__(self, content=None):
        super().__init__()
        self.content = content

    def __str__(self):
        return f"SingleQuoted(content={self.content})"

    def __eq__(self, other):
        return isinstance(other, SingleQuoted) and self.content == other.content

    def eval(self, input, output):
        pass

class DoubleQuoted(AbstractShellFeature):
    def __init__(self, content=None):
        super().__init__()
        self.content = content

    def __str__(self):
        return f"DoubleQuoted(content={self.content})"

    def __eq__(self, other):
        return isinstance(other, DoubleQuoted) and self.content == other.content

    def eval(self, input, output):
        pass

class BackQuoted(AbstractShellFeature):
    def __init__(self, content=None):
        super().__init__()
        self.content = content

    def __str__(self):
        return f"BackQuoted(content={self.content})"

    def __eq__(self, other):
        return isinstance(other, BackQuoted) and self.content == other.content

    def eval(self, input, output):
        pass
