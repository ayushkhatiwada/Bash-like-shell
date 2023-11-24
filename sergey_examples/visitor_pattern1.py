"""
Derivation of visitor pattern part 1:
The goal here is to remove the eval() function from the classes and move them outside
We can do this using the visitor pattern
"""


class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()

class Mult:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()

class Num():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

expr = Add(Mult(Num(2), Num(4)), Num(5)) # (2 * 4) + 5
ans = expr.eval()
print(ans)
