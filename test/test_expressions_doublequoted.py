import unittest
from unittest.mock import Mock
from expressions import DoubleQuoted


class TestDoubleQuoted(unittest.TestCase):
    def test_doublequoted_init(self):
        children = [Mock(), "text", Mock()]
        dq = DoubleQuoted(*children)
        self.assertEqual(dq.children, children)

    def test_doublequoted_eq(self):
        child1 = "text1"
        child2 = "text2"
        dq1 = DoubleQuoted(child1, child2)
        dq2 = DoubleQuoted(child1, child2)
        dq3 = DoubleQuoted(child2, child1)
        self.assertEqual(dq1, dq2)
        self.assertNotEqual(dq1, dq3)

    def test_doublequoted_eval(self):
        child1_mock = Mock()
        child1_mock.eval.return_value = "evaluated1"
        child2 = "text"
        child3_mock = Mock()
        child3_mock.eval.return_value = "evaluated2"
        dq = DoubleQuoted(child1_mock, child2, child3_mock)
        result = dq.eval()
        self.assertEqual(result, "evaluated1textevaluated2")
