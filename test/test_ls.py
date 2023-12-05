import os
import shutil
import unittest
from collections import deque


from applications.ls import Ls
from applications.application import ApplicationError


class TestLs(unittest.TestCase):
    TEST_DIR = "test_directory"
    ls_app = Ls()

    def setUp(self):
        """
        File Structure
        --------------
        test_directory
        ├── file1
        ├── file2
        ├── dir1
        │   ├── file3
        │   └── file4
        └── dir2
        """

        # Create the test directory
        os.mkdir(self.TEST_DIR)

        # Create empty files and directories inside the test directory
        open(os.path.join(self.TEST_DIR, "file1"), "w").close()
        open(os.path.join(self.TEST_DIR, "file2"), "w").close()

        os.mkdir(os.path.join(self.TEST_DIR, "dir1"))
        open(os.path.join(self.TEST_DIR, "dir1", "file3"), "w").close()
        open(os.path.join(self.TEST_DIR, "dir1", "file4"), "w").close()

        os.mkdir(os.path.join(self.TEST_DIR, "dir2"))

        os.chdir(self.TEST_DIR)

    def tearDown(self):
        # Clean up the test directory
        os.chdir("..")
        shutil.rmtree(self.TEST_DIR)

    def test_ls_default_directory(self):
        output = deque()
        self.ls_app.exec([], [], output)
        result = output.popleft()

        self.assertIn("file1", result)
        self.assertIn("file2", result)
        self.assertIn("dir1", result)
        self.assertIn("dir2", result)

    def test_ls_custom_directory(self):
        output = deque()
        self.ls_app.exec(["dir1"], [], output)
        result = output.popleft()

        self.assertIn("file3", result)
        self.assertIn("file4", result)

    def test_ls_file_not_found_error(self):
        with self.assertRaises(ApplicationError):
            self.ls_app.exec(["file1.txt"], [], deque())

    def test_ls_directory_not_found_error(self):
        with self.assertRaises(ApplicationError):
            self.ls_app.exec(["nonexistent_dir"], [], deque())
