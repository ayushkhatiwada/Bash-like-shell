import os
import unittest
import shutil
from collections import deque

from applications.find import Find
from applications.application import ArgumentError


class TestFind(unittest.TestCase):
    find_app = Find()

    def setUp(self):
        """
        File Structure
        --------------
        test_directory
        ├── file1.txt
        ├── file2.txt
        ├── file3.txt
        └──  dir1
            ├── file4.txt
            └── file5.txt
        """

        self.std_out = deque()
        self.TEST_DIR = "test_directory"

        # make test directory, go into it
        os.mkdir(self.TEST_DIR)
        os.chdir(self.TEST_DIR)

        # create files
        open("file1.txt", 'w').close()
        open("file2.txt", 'w').close()
        open("file3.txt", 'w').close()

        # create dir1, go into it, create files
        os.mkdir("dir1")
        os.chdir("dir1")
        open("file4.txt", 'w').close()
        open("file5.txt", 'w').close()

        # go back to test_directory
        os.chdir("..")

    def tearDown(self):
        # go back to parent directory, delete test_directory
        os.chdir("..")
        shutil.rmtree(self.TEST_DIR)

    def test_find_no_arguments(self):
        with self.assertRaises(ArgumentError):
            self.find_app.exec([], [], self.std_out)

    def test_find_too_many_arguments(self):
        with self.assertRaises(ArgumentError):
            self.find_app.exec(
                ["-name", "hehe", "haha", "hoho"], [], self.std_out
            )

    def test_find_no_name_flag(self):
        with self.assertRaises(ArgumentError):
            self.find_app.exec(["-noname"], [], self.std_out)

    def test_find_one_file(self):
        self.find_app.exec(["-name", "file1.txt"], [], self.std_out)
        self.assertEqual(self.std_out.popleft(), "./file1.txt\n")

    def test_find_file_in_subdirectory(self):
        self.find_app.exec(["-name", "file4.txt"], [], self.std_out)
        self.assertEqual(self.std_out.popleft(), "./dir1/file4.txt\n")
