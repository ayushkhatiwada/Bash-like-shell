import unittest
from unittest.mock import Mock
from collections import deque
import shell
from expressions import Seq

class TestSeq(unittest.TestCase):
    def test_seq_init(self):
        left_mock = Mock()
        right_mock = Mock()
        seq = Seq(left_mock, right_mock)
        self.assertEqual(seq.left, left_mock)
        self.assertEqual(seq.right, right_mock)

    def test_seq_str(self):
        left_mock = Mock()
        right_mock = Mock()
        left_mock.__str__ = Mock(return_value="LeftMock")
        right_mock.__str__ = Mock(return_value="RightMock")
        seq = Seq(left_mock, right_mock)
        self.assertEqual(str(seq), "Seq(LeftMock, RightMock)")

    def test_seq_eq(self):
        left_mock = Mock()
        right_mock = Mock()
        seq1 = Seq(left_mock, right_mock)
        seq2 = Seq(left_mock, right_mock)
        seq3 = Seq(right_mock, left_mock)
        self.assertEqual(seq1, seq2)
        self.assertNotEqual(seq1, seq3)

    def test_seq_eval(self):
        left_mock = Mock()
        right_mock = Mock()
        seq = Seq(left_mock, right_mock)
        output = deque()
        seq.eval(output)
        left_mock.eval.assert_called_once_with(output)
        right_mock.eval.assert_called_once_with(output)
