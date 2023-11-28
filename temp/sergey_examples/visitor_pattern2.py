"""
Derivation of visitor pattern part 2:
Here we are trying to move the eval function out of the classes

Notice how to the eval function has to check the type of the objects passed in
So it then knows what operator to use (+, *)
This is not good code
"""

from abc import ABC, abstractmethod


class AbstractOperator(ABC):
    pass

class Add(AbstractOperator):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    #   def eval(self):
    #     return self.left.eval() + self.right.eval()

class Mult(AbstractOperator):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    # def eval(self):
    #     return self.left.eval() * self.right.eval()


# Trying to extract eval function out of the classes
def eval(op: AbstractOperator):

    if isinstance(op, int):
        return op
    
    elif isinstance(op, Add):
        return eval(op.left) + eval(op.right)
    
    elif isinstance(op, Mult):
        return eval(op.left) * eval(op.right)


ans = eval(Mult(Add(3, 5), 4))
print(ans)
