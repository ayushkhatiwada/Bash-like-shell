import os
import shutil
import unittest
from collections import deque

from applications.application_unsafe import ApplicationUnsafe
from applications.ls import Ls


class TestApplicationUnsafe(unittest.TestCase):
    TEST_DIR = 'test_directory'
    unsafe_ls_app = ApplicationUnsafe(Ls())

    def setUp(self):
        # Create an empty test directory
        os.mkdir(self.TEST_DIR)

        os.chdir(self.TEST_DIR)

    def tearDown(self):
        # Clean up the test directory
        os.chdir('..')
        shutil.rmtree(self.TEST_DIR)

    def test_exception_printed_instead_of_raised(self):
        output = deque()
        self.unsafe_ls_app.exec(['file1'], [], output)
        result = output.popleft()

        # Check that the error message was printed
        self.assertIn('No such file or directory', result)
