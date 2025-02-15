import unittest
from collections import deque

import os
from applications.application import ApplicationError
from applications.sort import Sort


class TestSort(unittest.TestCase):
    sort_app = Sort()
    test_file_name = 'test_file.txt'
    test_content = ["apple\n", "banana\n", "cherry\n"]

    def setUp(self):
        with open(self.test_file_name, 'w') as file:
            file.writelines(self.test_content)

    def tearDown(self):
        os.remove(self.test_file_name)

    def test_sort_file(self):
        output = deque()
        self.sort_app.exec([self.test_file_name], [], output)
        result = ''.join(list(output))  # Join all lines in the output
        expected = ''.join(sorted(self.test_content))

        self.assertEqual(result, expected)

    def test_sort_stdin(self):
        output = deque()
        self.sort_app.exec([], self.test_content, output)
        result = ''.join(list(output))
        expected = '\n'.join(sorted(self.test_content)) + '\n'

        self.assertEqual(result, expected)

    def test_sort_reverse(self):
        output = deque()
        self.sort_app.exec(['-r', self.test_file_name], [], output)
        result = ''.join(list(output))
        expected = ''.join(sorted(self.test_content, reverse=True))

        self.assertEqual(result, expected)

    def test_sort_nonexistent_file_error(self):
        nonexistent_file = 'nonexistent_file.txt'
        with self.assertRaises(ApplicationError):
            self.sort_app.exec([nonexistent_file], [], deque())
