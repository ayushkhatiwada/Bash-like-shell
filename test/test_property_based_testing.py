import os
import unittest
import shutil
from collections import deque
from typing import List

from hypothesis import given, assume
from hypothesis.strategies import text, lists

from applications.application import ApplicationError
from applications.echo import Echo
from applications.cd import Cd
from applications.ls import Ls


class TestHyphotesisTesting(unittest.TestCase):
    TEST_DIR = "test_directory"

    def setUp(self):
        """
        File Structure
        --------------
        test_directory
        ├── file1
        ├── dir1
        │   ├── file2
        │   └── file3
        └── dir2
        """

        # Create the test directory
        os.mkdir(self.TEST_DIR)

        # Create empty files and directories inside the test directory
        open(os.path.join(self.TEST_DIR, "file1"), "w").close()

        os.mkdir(os.path.join(self.TEST_DIR, "dir1"))
        open(os.path.join(self.TEST_DIR, "dir1", "file2"), "w").close()
        open(os.path.join(self.TEST_DIR, "dir1", "file3"), "w").close()

        os.mkdir(os.path.join(self.TEST_DIR, "dir2"))

        # Go into the test directory
        os.chdir(self.TEST_DIR)

    def tearDown(self):
        # Clean up the test directory
        os.chdir("..")
        shutil.rmtree(self.TEST_DIR)

    @given(lists(text().filter(lambda x: "\r" not in x)))
    def test_echo(self, args: List[str]):
        assume(args)

        echo = Echo()
        output = deque()
        # Call the exec method with the generated args
        echo.exec(args, [], output)

        result = ' '.join(args) + '\n'
        # Check that the result is equal to the joined args
        self.assertEqual(output.pop(), result)

    @given(text().filter(lambda x: "\r" not in x))
    def test_echo_ends_with_new_line(self, args: List[str]):
        echo = Echo()
        assume(args)

        output = deque()
        echo.exec([args], [], output)
        self.assertTrue(output.pop().endswith('\n'))

    @given(text())
    def test_cd_raises_no_such_file_or_directory_error(self, directory: str):
        cd = Cd()
        # assuming directory is alphanumeric removes the possibility of
        # having a directory with characters that are not allowed in
        # directory names e.g.
        # / (forward slash)
        # The NULL character (\0)
        assume(
            directory.isalnum() and not os.path.isdir(directory))

        with self.assertRaises(ApplicationError):
            cd.exec([directory], [], deque())

    @given(text())
    def test_ls_raises_no_such_file_or_directory_error(self, directory: str):
        ls = Ls()
        assume(directory.isalnum() and not os.path.isdir(directory))

        with self.assertRaises(ApplicationError):
            ls.exec([directory], [], deque())


if __name__ == '__main__':
    unittest.main()
