"""
Part 3: Sergey's implementation of visitor pattern
We have moved the eval out of the classes
and we don't have lots of if else statements

This code is a bit tricky to understand 
Go through step by step and slowly understand what's going on

An instance of EvalVisitor is passed around
So the appropriate visit method can be called
"""

class Expr:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def accept(self, visitor):
        pass

class Add(Expr):
    def __init__(self, left, right):
        super().__init__(left, right)

    def accept(self, visitor):
        return visitor.visitAdd(self)

class Mult(Expr):
    def __init__(self, left, right):
        super().__init__(left, right)

    def accept(self, visitor):
        return visitor.visitMult(self)

class EvalVisitor:

    def visitAdd(self, a):
        return a.left.accept(self) + a.right.accept(self)
    
    def visitMult(self, a):
        return a.left.accept(self) * a.right.accept(self)


evaluator = EvalVisitor()
expr = Mult(Add(3, 5), 4)
print(expr.accept(evaluator))


def eval(expr: Expr):
    evaluator = EvalVisitor()
    return expr.accept(evaluator)
