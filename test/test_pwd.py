import os
import unittest
from collections import deque

from applications.application import ApplicationError
from applications.pwd import Pwd


class TestPwd(unittest.TestCase):
    pwd_app = Pwd()

    def setUp(self):
        self.original_dir = os.getcwd()
        self.test_dir = 'test_directory'
        os.mkdir(self.test_dir)
        os.chdir(self.test_dir)

    def tearDown(self):
        os.chdir(self.original_dir)
        os.rmdir(self.test_dir)

    def test_pwd_output(self):
        output = deque()
        self.pwd_app.exec([], [], output)
        result = output.popleft()
        expected_output = os.path.join(self.original_dir, self.test_dir) + '\n'

        self.assertEqual(result, expected_output)

    def test_pwd_with_args(self):
        output = deque()
        self.pwd_app.exec(['argument'], [], output)
        result = output.popleft()
        expected_output = os.path.join(self.original_dir, self.test_dir) + '\n'

        self.assertEqual(result, expected_output)
