import os
import unittest
from collections import deque

from applications.application import ApplicationError
from applications.tail import Tail


class TestTail(unittest.TestCase):
    TEST_FILE = 'test_file.txt'
    tail_app = Tail()

    def setUp(self):
        with open(self.TEST_FILE, 'w') as file:
            for i in range(1, 6):
                file.write(f"Line {i}\n")

    def tearDown(self):
        os.remove(self.TEST_FILE)

    def test_tail_default_behavior(self):
        output = deque()
        self.tail_app.exec([self.TEST_FILE], [], output)
        result = output.popleft().strip()  # Stripping the newline character
        expected = "Line 1\nLine 2\nLine 3\nLine 4\nLine 5"
        self.assertEqual(result, expected)

    def test_tail_n0(self):
        output = deque()
        self.tail_app.exec(['-n', '0', self.TEST_FILE], [], output)
        self.assertEqual(len(output), 0)

    def test_tail_more_lines_than_file_contains(self):
        output = deque()
        self.tail_app.exec(['-n', '10', self.TEST_FILE], [], output)
        result = output.popleft().strip()
        expected = "Line 1\nLine 2\nLine 3\nLine 4\nLine 5"
        self.assertEqual(result, expected)

    def test_tail_custom_lines(self):
        output = deque()
        self.tail_app.exec(['-n', '3', self.TEST_FILE], [], output)
        result = output.popleft().strip()
        expected = "Line 3\nLine 4\nLine 5"
        self.assertEqual(result, expected)

    def test_tail_file_not_found_error(self):
        with self.assertRaises(ApplicationError):
            self.tail_app.exec(['nonexistent_file.txt'], [], deque())

    def test_tail_invalid_lines_argument(self):
        with self.assertRaises(ApplicationError):
            self.tail_app.exec(['-n', 'abc', self.TEST_FILE], [], deque())

    def test_tail_from_stdin(self):
        input_data = ["Stdin Line 1\n", "Stdin Line 2\n", "Stdin Line 3\n"]
        output = deque()
        self.tail_app.exec(['-n', '2'], input_data, output)
        result = output.popleft().strip()
        expected = "Stdin Line 2\n\nStdin Line 3"
        self.assertEqual(result, expected)

    def test_tail_unexpected_error(self):
        bad_input = 123

        with self.assertRaises(ApplicationError):
            self.tail_app.exec([], bad_input, deque())
