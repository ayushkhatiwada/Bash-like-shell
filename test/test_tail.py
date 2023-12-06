import os
import shutil
import unittest
from collections import deque

from applications.application import ApplicationError
from applications.tail import Tail


class TestTail(unittest.TestCase):
    TEST_FILE = 'test_file.txt'
    tail_app = Tail()

    def setUp(self):
        """
        File Content
        ------------
        test_file.txt
            Line 1
            Line 2
            Line 3
            Line 4
            Line 5
        """
        # Create the test file with specified content
        with open(self.TEST_FILE, 'w') as file:
            for i in range(1, 6):
                file.write(f"Line {i}\n")

    def tearDown(self):
        # Clean up the test file
        os.remove(self.TEST_FILE)

    def test_tail_default_lines(self):
        output = deque()
        self.tail_app.exec([self.TEST_FILE], [], output)
        result = output.popleft()

        self.assertIn('Line 1', result)
        self.assertIn('Line 5', result)

    def test_tail_custom_lines(self):
        output = deque()
        self.tail_app.exec(['-n3', self.TEST_FILE], [], output)
        result = output.popleft()

        self.assertNotIn('Line 2', result)
        self.assertIn('Line 3', result)
        self.assertIn('Line 4', result)
        self.assertIn('Line 5', result)

    def test_tail_file_not_found_error(self):
        with self.assertRaises(ApplicationError):
            self.tail_app.exec(['nonexistent_file.txt'], [], deque())

    def test_tail_invalid_lines_argument(self):
        with self.assertRaises(ApplicationError):
            self.tail_app.exec(['-nabc', self.TEST_FILE], [], deque())

    def test_tail_from_stdin(self):
        input_data = deque(["Stdin Line 1\n", "Stdin Line 2\n", "Stdin Line 3\n"])
        output = deque()
        self.tail_app.exec(['-n2'], input_data, output)
        result = output.popleft()

        self.assertNotIn('Stdin Line 1', result)
        self.assertIn('Stdin Line 2', result)
        self.assertIn('Stdin Line 3', result)
