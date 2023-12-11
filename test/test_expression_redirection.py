import unittest
from unittest.mock import Mock
import shell
from expressions import Redirection

class TestRedirection(unittest.TestCase):
    def test_redirection_init(self):
        argument_mock = Mock()
        redir = Redirection("<", argument_mock)
        self.assertEqual(redir.type, "<")
        self.assertEqual(redir.argument, argument_mock)

    def test_redirection_str(self):
        argument_mock = Mock()
        argument_mock.__str__ = Mock(return_value="ArgumentMock")
        redir = Redirection("<", argument_mock)
        self.assertEqual(str(redir), "Redirection(<, ArgumentMock)")

    def test_redirection_eq(self):
        argument_mock1 = Mock()
        argument_mock2 = Mock()
        redir1 = Redirection("<", argument_mock1)
        redir2 = Redirection("<", argument_mock1)
        redir3 = Redirection(">", argument_mock2)
        self.assertEqual(redir1, redir2)
        self.assertNotEqual(redir1, redir3)

    def test_redirection_eval(self):
        argument_mock = Mock()
        redir = Redirection("<", argument_mock)
        argument_mock.eval.return_value = "evaluated_argument"
        result = redir.eval()
        self.assertEqual(result, redir)
        argument_mock.eval.assert_called_once()
        self.assertEqual(redir.argument, "evaluated_argument")
