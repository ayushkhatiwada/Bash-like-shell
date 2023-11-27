from visitor import Visitor


class AbstractCommand:
    def __init__(self) -> None:
        pass


# change accept commands to execute???

# I don't think it should be called command
# Should be called a command of commands - or a better name entirely
# This is a non base case command
# Should be an abstract class as well I think
class Commmand:
    
    def accept(self, visitor):
        return visitor.visit_command(self)


class Pipe:
    # check type hints with HJP/XLow
    def __init__(self, left_side, right_side: Commmand):
        self.left_side = left_side
        self.right_side = right_side

    def accept(self, visitor: Visitor):
        return visitor.visit_pipe(self) 


class Seq:
    
    def accept(self, visitor):
        return visitor.visit_seq(self)


# I think this is the base case
# Call represents ONE specific command (cat) and it's, one or more, input arguments (file1.txt, file2.txt)
class Call:
    
    def accept(self, visitor):
        return visitor.visit_call(self)









class DoubleQuote:
    pass



# I don't think argument is needed, only pipe, seq, and call
# Call seems to be the base case
# Because call contains your specific command (cat, ls) and the specific arguments need (file.txt)
# that's all you need to execute
class Argument:

    def accept(self, visitor):
        return visitor.visit_argument(self)
    

# Note: not sure how to handle redirection or command substitution
