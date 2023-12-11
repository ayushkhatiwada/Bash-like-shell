import unittest
from unittest.mock import Mock, patch
from collections import deque
import shell
from expressions import BackQuoted

class TestBackQuoted(unittest.TestCase):
    def test_backquoted_init(self):
        child_mock = Mock()
        bq = BackQuoted(child_mock)
        self.assertEqual(bq.child, child_mock)

    def test_backquoted_str(self):
        child_mock = Mock()
        child_mock.__str__ = Mock(return_value="ChildMock")
        bq = BackQuoted(child_mock)
        self.assertEqual(str(bq), "BackQuoted(ChildMock)")

    def test_backquoted_eq(self):
        child_mock1 = Mock()
        child_mock2 = Mock()
        bq1 = BackQuoted(child_mock1)
        bq2 = BackQuoted(child_mock1)
        bq3 = BackQuoted(child_mock2)
        self.assertEqual(bq1, bq2)
        self.assertNotEqual(bq1, bq3)

    @patch('expressions.shell')
    def test_backquoted_eval(self, mock_shell):
        child_mock = Mock()
        converted_expression_mock = Mock()
        mock_shell.convert.return_value = converted_expression_mock

        converted_expression_mock.eval = Mock()
        output_data = deque(["line1\n", "line2\n"])
        converted_expression_mock.eval.side_effect = lambda output: output.extend(output_data)

        bq = BackQuoted(child_mock)
        result = bq.eval()

        mock_shell.convert.assert_called_once_with(child_mock)
        converted_expression_mock.eval.assert_called_once()
        self.assertEqual(result, "line1\nline2")
