import os
import shutil
import unittest
from collections import deque

from applications.application import ApplicationError, ArgumentError
from applications.grep import Grep


class TestGrep(unittest.TestCase):
    TEST_DIR = 'test_grep_directory'
    grep_app = Grep()

    def setUp(self):
        """
            File Structure
            --------------
            test_grep_directory
            ├── file1 (contains 'hello world')
            ├── file2 (contains 'goodbye world')
        """

        os.mkdir(self.TEST_DIR)

        with open(os.path.join(self.TEST_DIR, 'file1'), 'w') as f:
            f.write('hello world\nanother line\n')

        with open(os.path.join(self.TEST_DIR, 'file2'), 'w') as f:
            f.write('goodbye world\nanother goodbye\n')

        os.chdir(self.TEST_DIR)

    def tearDown(self):
        os.chdir('..')
        shutil.rmtree(self.TEST_DIR)

    def test_grep_pattern_in_file(self):
        output = deque()
        self.grep_app.exec(['world', 'file1', 'file2'], [], output)
        result = '\n'.join(output)

        self.assertIn('file1:hello world', result)
        self.assertIn('file2:goodbye world', result)

    def test_grep_pattern_not_in_file(self):
        output = deque()
        self.grep_app.exec(['not_in_file'], [], output)
        self.assertEqual(len(output), 0)

    def test_grep_invalid_regex(self):
        with self.assertRaises(ApplicationError):
            self.grep_app.exec(['\\'], [], deque())

    def test_grep_no_pattern_provided(self):
        with self.assertRaises(ArgumentError):
            self.grep_app.exec([], [], deque())

    def test_grep_pattern_found_in_file(self):
        output = deque()

        self.grep_app.exec(['hello', 'file1'], [], output)
        self.assertIn('hello world\n', output)
        output.clear()

        self.grep_app.exec(['goodbye', 'file2'], [], output)
        self.assertIn('goodbye world\n', output)

    def test_grep_pattern_not_found_in_file(self):
        output = deque()
        self.grep_app.exec(['notfound'], [], output)
        self.assertEqual(len(output), 0)

    def test_grep_pattern_found_in_specific_file(self):
        output = deque()
        pattern = 'hello'
        expected_line = 'hello world\n'

        self.grep_app.exec([pattern, 'file1'], [], output)

        found = any(
            expected_line in line and 'file1:' in line for line in output
        )
        self.assertFalse(found, f"Pattern '{pattern}' was not found in 'file1'")

    def test_grep_file_not_found(self):
        output = deque()
        with self.assertRaises(ApplicationError):
            self.grep_app.exec(['hello', 'nonexistent_file'], [], output)

    def test_grep_stdin(self):
        input_data = ['hello world', 'goodbye world', 'some other line']
        output = deque()
        self.grep_app.exec(['world'], input_data, output)
        result = '\n'.join(output)

        self.assertIn('hello world', result)
        self.assertIn('goodbye world', result)
        self.assertNotIn('some other lines', result)


if __name__ == '__main__':
    unittest.main()
