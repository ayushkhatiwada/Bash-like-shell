from visitor import Visitor


# change accept commands to execute???
class AbstractCommand:
    def __init__(self) -> None:
        pass


# I don't think it should be called command
# Should be called a command of commands - or a better name entirely
# This is a non base case command
class Commmand(AbstractCommand):
    
    def accept(self, visitor):
        return visitor.visit_command(self)


class Pipe(AbstractCommand):
    # check type hints with HJP/XLow
    def __init__(self, left_side, right_side: Commmand):
        self.left_side = left_side
        self.right_side = right_side

    def accept(self, visitor: Visitor):
        return visitor.visit_pipe(self) 


class Seq(AbstractCommand):
    
    def accept(self, visitor):
        return visitor.visit_seq(self)


# I think this is the base case
# Call represents ONE specific command (cat) and it's, one or more, input arguments (file1.txt, file2.txt)
class Call(AbstractCommand):
    
    def accept(self, visitor):
        return visitor.visit_call(self)


class Atom:
    pass


class Argument:
    
    def accept(self, visitor):
        return visitor.visit_argument(self)


class Redirection:
    pass


class Quoted:
    pass


class SingleQuoted:
    pass


class BackQuoted:
    pass


class DoubleQuoted:
    pass




# Note: not sure how to handle redirection or command substitution