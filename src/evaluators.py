from commands import *
from visitor import Visitor


class Evaluator(Visitor):
    def visit_command(self, a):
        pass

    # if you have reached here
    # you know 
    def visit_pipe(self: Visitor, command: Pipe) -> Commmand:

        # evaluate left side while continuing to pass around visitor
        left_side_std_out = command.left_side.accept(self)
        return command.right_side

    def visit_seq(self, a):
        pass

    def visit_call(self, a):
        pass


    
    # don't think this is needed
    def visit_argument(self, a):
        pass
