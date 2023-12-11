import os
import shutil
import unittest
from collections import deque

from applications.cat import Cat
from applications.application import ApplicationError


class TestCat(unittest.TestCase):
    cat_app = Cat()

    def setUp(self):
        """
        File Structure
        --------------
        test_directory
        ├── file1.txt
        ├── file2.txt
        └── file3.txt
        """

        self.std_out = deque()
        self.TEST_DIR = "test_directory"
        # make test directory
        os.mkdir(self.TEST_DIR)

        self.files = {
            "file1.txt": "this\nis\nfile\nnumber\none\n",
            "file2.txt": "and\nthis\nis\nthe\nsecond\nfile\n",
            "file3.txt": "third\nfile\nto\ntest\nmultiple\nfiles\n",
        }

        # Create files in test driectory and write content
        for filename, content in self.files.items():
            with open(os.path.join(self.TEST_DIR, filename), "x") as f:
                f.write(content)

        # Change the working directory to the test directory
        os.chdir(self.TEST_DIR)

    # Clean up the test directory
    def tearDown(self):
        # Leave the test directory
        os.chdir("..")
        # Delete test directory and its contents recursively
        shutil.rmtree(self.TEST_DIR)

    def test_cat_single_file(self):
        self.cat_app.exec(["file1.txt"], [], self.std_out)
        ans = self.files["file1.txt"].split()
        self.assertListEqual(list(self.std_out), [line + "\n" for line in ans])

    def test_cat_std_in(self):
        std_in = ["Sergey", "is", "a", "cool", "teacher"]
        self.cat_app.exec([], std_in, self.std_out)
        expected_output = [line + "\n" for line in std_in]
        self.assertListEqual(list(self.std_out), expected_output)

    def test_cat_two_files(self):
        args = ["file1.txt", "file2.txt"]
        self.cat_app.exec(args, [], self.std_out)

        files = [self.files[arg] for arg in args]
        ans = "".join(files).split()
        self.assertListEqual(list(self.std_out), [line + "\n" for line in ans])

    def test_cat_multiple_files(self):
        args = ["file1.txt", "file2.txt", "file3.txt"]
        self.cat_app.exec(args, [], self.std_out)

        files = [self.files[arg] for arg in args]
        ans = "".join(files).split()
        self.assertListEqual(list(self.std_out), [line + "\n" for line in ans])

    def test_cat_file_not_found_error(self):
        with self.assertRaises(ApplicationError):
            self.cat_app.exec(["file1"], [], self.std_out)
