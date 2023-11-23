"""
Use visitor pattern and implement commands in CommandGrammar Parser Rules
"""
from antlr.CommandGrammarLexer import C

class Visitor(CommandGrammarVisitor):
    def visitCommand(ctx):
        return self.visitChildren(ctx)

    def visitSeq(self, ctx):
        for child in ctx.getChildren():
            self.visit(child)



"""
How to start:
--------------
- Look at generated antlr files
- look at context
- look at visitor & visotr children

- think of it recursively 


# Take a look at fucntions in generated files
# self.visit self.visitchildren

"""