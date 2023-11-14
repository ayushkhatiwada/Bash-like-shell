# First example from lecture 4, this has issues and should not be used

class Add:
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub:
    def eval(self):
        return self.left.eval() - self.right.eval()


class Mult:
    def eval(self):
        return self.left.eval() * self.right.eval()


expr = Add(Mult(2, 4), 5) # (2*4) + 5
expr.eval()


def eval(a: Add):
    return eval(a.left) + eval(a.right)

def eval(a: Mult):
    return eval(a.left) * eval(a.right)

def evalAdd(a):
    return eval(a.left) + eval(a.right)


# This is bad, uses if else statements 
def evalMult(a):
    if isinstance(a.left, Mult):
        left = evalMult(a.left)
    if isinstance(a.left, Add):
        left = evalAdd(a.left)
        ...
    # return left * right

