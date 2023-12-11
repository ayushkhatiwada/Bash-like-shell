import unittest
from collections import deque

from applications.application import ApplicationError
from applications.uniq import Uniq
from unittest.mock import mock_open, patch


class TestUniq(unittest.TestCase):
    uniq_app = Uniq()

    def setUp(self):
        """
        Set up input data for testing.
        """
        self.input_data = [
            "Line1\n",
            "Line2\n",
            "Line2\n",
            "line2\n",
            "Line3\n"
        ]

    def test_uniq_basic(self):
        output = deque()
        self.uniq_app.exec([], self.input_data, output)
        result = ''.join(output)

        expected_output = "Line1\n\nLine2\n\nline2\n\nLine3\n\n"
        self.assertEqual(result, expected_output)

    def test_uniq_ignore_case(self):
        output = deque()
        self.uniq_app.exec(['-i'], self.input_data, output)
        result = ''.join(output)

        expected_output = "Line1\n\nLine2\n\nLine3\n\n"
        self.assertEqual(result, expected_output)

    def test_uniq_file_not_found_error(self):
        with self.assertRaises(ApplicationError):
            self.uniq_app.exec(['nonexistent_file'], [], deque())

    def test_uniq_read_from_file(self):
        mocked_file_content = "Line1\nLine2\nLine2\n"
        with patch('builtins.open', mock_open(read_data=mocked_file_content)):
            output = deque()
            self.uniq_app.exec(['test_file.txt'], [], output)
            result = ''.join(output)

            expected_output = "Line1\nLine2\n"
            self.assertEqual(result, expected_output)

    def test_uniq_generic_exception_handling(self):
        with patch('applications.uniq.open', side_effect=Exception(
                "Test Exception")):
            with self.assertRaises(ApplicationError):
                self.uniq_app.exec(['test_file.txt'], [], deque())

    def test_uniq_empty_input(self):
        output = deque()
        self.uniq_app.exec([], [], output)
        self.assertEqual(len(output), 0)
