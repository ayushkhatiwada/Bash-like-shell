import unittest
from unittest.mock import MagicMock
from expressions import Commmand, Pipe, Seq, Call
from converter import Converter
from antlr.ShellGrammarParser import ShellGrammarParser

class TestConverter(unittest.TestCase):
    def setUp(self):
        self.converter = Converter()
        self.command_context_mock = MagicMock()

    def test_visit_pipe(self):
        left_call_context_mock = MagicMock(spec=ShellGrammarParser.CallContext)
        right_call_context_mock = MagicMock(spec=ShellGrammarParser.CallContext)
        pipe_context_mock = MagicMock(spec=ShellGrammarParser.PipeContext)
        pipe_context_mock.children = [left_call_context_mock, '|', right_call_context_mock]

        self.converter.visitCall = MagicMock(return_value="mocked value")
        result = self.converter.visitPipe(pipe_context_mock)
        self.assertIsInstance(result, Pipe)

if __name__ == '__main__':
    unittest.main()
