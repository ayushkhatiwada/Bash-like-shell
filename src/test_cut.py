import unittest
from collections import deque
from io import StringIO
import sys
from unittest import mock


from applications.cut import Cut
from applications.application import ApplicationError


class TestCut(unittest.TestCase):
    cut_app = Cut()

    def setUp(self):
        # Redirect stdout to capture output for testing
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        # Reset stdout after tests
        sys.stdout = self.held

    def test_cut_specific_bytes(self):
        output = deque()
        input_data = ['abcdefg\n', 'hijklmn\n']
        self.cut_app.exec(['-b', '1,3,5', 'stdin'], input_data, output)
        result = ''.join(output)

        self.assertEqual(result, 'ace\nhjl\n')

    def test_cut_byte_range(self):
        output = deque()
        input_data = ['abcdefg\n', 'hijklmn\n']
        self.cut_app.exec(['-b', '2-4', 'stdin'], input_data, output)
        result = ''.join(output)

        self.assertEqual(result, 'bcd\nijk\n')

    def test_cut_with_file(self):
        output = deque()
        test_file_content = 'line1\nline2\nline3\n'
        with mock.patch('builtins.open', mock.mock_open(read_data=test_file_content)):
            self.cut_app.exec(['-b', '1-3', 'test_file.txt'], [], output)
            result = ''.join(output)

        self.assertEqual(result, 'lin\nlin\nlin\n')

    def test_cut_invalid_option(self):
        with self.assertRaises(ApplicationError):
            self.cut_app.exec(['-c', '1-3'], [], deque())

    def test_cut_invalid_byte_range(self):
        with self.assertRaises(ValueError):
            self.cut_app.exec(['-b', 'abc'], [], deque())

    def test_cut_no_arguments(self):
        with self.assertRaises(ApplicationError):
            self.cut_app.exec([], [], deque())

    def test_cut_insufficient_arguments(self):
        with self.assertRaises(ApplicationError):
            self.cut_app.exec(['-b'], [], deque())

    def test_cut_from_list_input(self):
        output = deque()
        input_data = ['line1\n', 'line2\n', 'line3\n']
        self.cut_app.exec(['-b', '1-3', 'stdin'], input_data, output)
        result = ''.join(output)

        self.assertEqual(result, 'lin\nlin\nlin\n')

    def test_cut_file_not_found_error(self):
        output = deque()
        with self.assertRaises(ApplicationError) as context:
            self.cut_app.exec(['-b', '1-3', 'nonexistent_file.txt'], [], output)

        self.assertTrue('nonexistent_file.txt: Unable to read file or input.' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
