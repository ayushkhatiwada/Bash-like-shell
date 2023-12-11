import unittest
from unittest.mock import Mock
from collections import deque
import shell
from expressions import Pipe


class TestPipe(unittest.TestCase):
    def test_pipe_init(self):
        left_mock = Mock()
        right_mock = Mock()
        pipe = Pipe(left_mock, right_mock)
        self.assertEqual(pipe.left, left_mock)
        self.assertEqual(pipe.right, right_mock)

    def test_pipe_str(self):
        left_mock = Mock()
        right_mock = Mock()
        left_mock.__str__ = Mock(return_value="LeftMock")
        right_mock.__str__ = Mock(return_value="RightMock")
        pipe = Pipe(left_mock, right_mock)
        self.assertEqual(str(pipe), "Pipe(LeftMock, RightMock)")

    def test_pipe_eq(self):
        left_mock = Mock()
        right_mock = Mock()
        pipe1 = Pipe(left_mock, right_mock)
        pipe2 = Pipe(left_mock, right_mock)
        pipe3 = Pipe(right_mock, left_mock)
        self.assertEqual(pipe1, pipe2)
        self.assertNotEqual(pipe1, pipe3)

    def test_pipe_eval(self):
        left_mock = Mock()
        right_mock = Mock()
        pipe = Pipe(left_mock, right_mock)
        output = deque()
        input = deque(['input_data'])
        pipe.eval(output, input)
        left_mock.eval.assert_called_once_with(deque(), input)
        right_mock.eval.assert_called_once_with(output, input=deque())
