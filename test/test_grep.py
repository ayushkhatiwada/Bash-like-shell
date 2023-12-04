import os
import shutil
import unittest
from collections import deque

from applications.application import ApplicationError
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

        # Create the test directory
        os.mkdir(self.TEST_DIR)

        # Create files with content
        with open(os.path.join(self.TEST_DIR, 'file1'), 'w') as f:
            f.write('hello world\nanother line\n')

        with open(os.path.join(self.TEST_DIR, 'file2'), 'w') as f:
            f.write('goodbye world\nanother goodbye\n')

        os.chdir(self.TEST_DIR)

    def tearDown(self):
        # Clean up the test directory
        os.chdir('..')
        shutil.rmtree(self.TEST_DIR)

    def test_grep_pattern_in_file(self):
        output = deque()
        self.grep_app.exec(['world'], [], output)
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
        with self.assertRaises(ApplicationError):
            self.grep_app.exec([], [], deque())

    def test_grep_pattern_found_in_file(self):
        output = deque()
        self.grep_app.exec(['hello'], [], output)
        self.assertIn('file1:hello world\n', output)
        output.clear()

        self.grep_app.exec(['goodbye'], [], output)
        self.assertIn('file2:goodbye world\n', output)

    def test_grep_pattern_not_found_in_file(self):
        output = deque()
        self.grep_app.exec(['notfound'], [], output)
        self.assertEqual(len(output), 0)

    def test_grep_pattern_found_in_specific_file(self):
        # Setup
        output = deque()
        pattern = 'hello'
        expected_line = 'hello world\n'  # Adjust this line to match exactly what's in the file

        # Execute
        self.grep_app.exec([pattern, 'file1'], [], output)

        # Verify
        found = any(expected_line in line and 'file1:' in line for line in output)
        self.assertTrue(found, f"Pattern '{pattern}' was not found in 'file1'")

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
        self.assertNotIn('some other line', result)

if __name__ == '__main__':
    unittest.main()
