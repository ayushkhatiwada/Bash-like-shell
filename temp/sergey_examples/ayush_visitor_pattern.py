"""
Ignore this
Ayush's attempt at moving the exec function out of the classes
"""


class OperatorVisitor:

    def visit_add(self):
        return eval(self.left) + eval(self.right)

    def visit_mult(self):
        return eval(self.left) * eval(self.right)


class Add(OperatorVisitor):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.visit_add()


class Mult(OperatorVisitor):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.visit_mult()


class Num():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value


def eval(op):
    return op.eval()

ans = eval(Mult(Add(Num(3), Num(5)), Num(4)))
print(ans)
