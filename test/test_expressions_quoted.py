import unittest
from unittest.mock import Mock
import shell
from expressions import Quoted


class TestQuoted(unittest.TestCase):
    def test_quoted_eval(self):
        child_mock = Mock()
        child_mock.eval.return_value = "evaluated_child"

        quoted = Quoted(child_mock)

        result = quoted.eval()
        self.assertEqual(result, "evaluated_child")

        child_mock.eval.assert_called_once()
