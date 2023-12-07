import unittest

from antlr4 import CommonTokenStream, InputStream
from antlr.ShellGrammarLexer import ShellGrammarLexer
from antlr.ShellGrammarParser import ShellGrammarParser
from converter import Converter


class TestConverter(unittest.TestCase):
    def strToExpression(self, cmd_line: str):
        lexer = ShellGrammarLexer(InputStream(cmd_line))
        tokens = CommonTokenStream(lexer)
        parser = ShellGrammarParser(tokens)

        tree = parser.command()
        expression = tree.accept(Converter())

        return expression

    def test_converting_single_command(self):
        cmd_line = "echo hello"
        expression = self.strToExpression(cmd_line)

        self.assertEqual(
            str(expression),
            "Command(Call(Argument(echo), Atom(Argument(hello))))"
        )
