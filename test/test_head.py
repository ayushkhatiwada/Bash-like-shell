import os
import shutil
import unittest
from collections import deque
from unittest.mock import patch

from applications.application import ApplicationError
from applications.head import Head


class TestHead(unittest.TestCase):
    TEST_DIR = "test_directory"
    TEST_FILE = "test_file.txt"
    head_app = Head()

    def setUp(self):
        # Create the test directory and file
        os.mkdir(self.TEST_DIR)
        with open(os.path.join(self.TEST_DIR, self.TEST_FILE), "w") as file:
            file.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5\n")
        os.chdir(self.TEST_DIR)

    def tearDown(self):
        # Clean up the test directory
        os.chdir("..")
        shutil.rmtree(self.TEST_DIR)

    def test_head_default_lines_from_file(self):
        output = deque()
        self.head_app.exec([self.TEST_FILE], [], output)
        result = "".join(output)

        self.assertEqual(result.count("\n"), 5)
        self.assertIn("Line 1", result)

    def test_head_specified_lines_from_file(self):
        output = deque()
        self.head_app.exec(["-n2", self.TEST_FILE], [], output)
        result = output.popleft()

        self.assertEqual(result, "Line 1\nLine 2\n")

    def test_head_from_stdin(self):
        output = deque()
        input_data = ["Line 1\n", "Line 2\n", "Line 3\n"]
        self.head_app.exec(["-n2"], input_data, output)
        result = output.popleft()

        self.assertEqual(result, "Line 1\nLine 2\n")

    def test_head_file_not_found_error(self):
        with self.assertRaises(ApplicationError):
            self.head_app.exec(["nonexistent_file.txt"], [], deque())

    def test_head_invalid_lines_argument(self):
        with self.assertRaises(ApplicationError):
            self.head_app.exec(["-na"], [], deque())

    def test_head_generic_exception(self):
        with patch("builtins.open", side_effect=OSError("Simulated Error")):
            with self.assertRaises(ApplicationError) as context:
                self.head_app.exec([self.TEST_FILE], [], deque())

            self.assertIn(
                "An error occurred: Simulated Error", str(context.exception)
            )
