"""
Improved method using visitor pattern
Use vistor pattern structure for shell commands in cwk

4 * 5 + 1 -> Add(Mult(4, 5), 1)

cat file.txt | grep abc; echo hello ->
    Seq(   Pipe(  Call( "cat", ["file.txt"] ), Call( "grep", ["abc"] )  ), Call( "echo", ["hello"] )   )
"""


class Expr:
    def accept(self, visitor):
        pass


class Add(Expr):
    def accept(self, visitor):
        return visitor.visitAdd(self)


class Sub(Expr):
    def accept(self, visitor):
        return visitor.visitSub(self)


class Mult(Expr):
    def accept(self, visitor):
        return visitor.visitMult(self)


class EvalVisitor:
    def visit_add(self, a):
        return a.left.accept(self) + a.right.accpet(self)

    def visit_sub(self, a):
        return a.left.accept(self) - a.right.accept(self)
    
    def visit_mult(self, a):
        return a.left.accept(self) * a.right.accept(self)


expr = None
evaluator = EvalVisitor()
print(expr.accept(evaluator))
