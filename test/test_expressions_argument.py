import unittest
from unittest.mock import Mock
import shell
from expressions import Argument, Quoted

class TestArgument(unittest.TestCase):
    def test_argument_eval_with_quoted_child(self):
        quoted_child_mock = Mock(spec=Quoted)
        quoted_child_mock.eval.return_value = "evaluated_quoted_child"

        string_child = "string_child"

        argument = Argument(quoted_child_mock, string_child)

        result = argument.eval()
        self.assertEqual(result, "evaluated_quoted_childstring_child")

        quoted_child_mock.eval.assert_called_once()
