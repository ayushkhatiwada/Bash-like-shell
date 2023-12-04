import os
import unittest
import shutil
from collections import deque

from applications.cd import Cd
from applications.application import ApplicationError


class TestCd(unittest.TestCase):
    cd_app = Cd()

    def setUp(self):
        """
        File Structure
        --------------
        test_directory
        ├── dir1
        ├── permission_denied_dir
        └──file.txt

        permission_denied_dir only created in test_cd_permission_denied_error
        """

        self.std_out = deque()
        self.TEST_DIR = "test_directory"
        self.dir1 = "dir1"
        self.file = "file.txt"

        # make test directory, go into it
        os.mkdir(self.TEST_DIR)
        os.chdir(self.TEST_DIR)

        # store path to dir1 (note: we are in test_directory)
        os.mkdir(self.dir1)
        self.dir1_path = os.path.join(os.getcwd(), self.dir1)

        # this creates file.txt in test_directory
        with open(self.file, 'w'):
            pass

    def tearDown(self):
        os.chdir("..")
        shutil.rmtree(self.TEST_DIR)

    def test_cd_no_arguments(self):
        initial_dir = os.getcwd()
        self.cd_app.exec([], [], self.std_out)
        self.assertEqual(initial_dir, os.getcwd())

    def test_cd_too_many_arguments(self):
        with self.assertRaises(ApplicationError):
            self.cd_app.exec(["dir1", "dir2"], [], self.std_out)

    def test_cd_one_valid_argument(self):
        self.cd_app.exec([self.dir1], [], self.std_out)
        self.assertEqual(os.getcwd(), self.dir1_path)
        os.chdir("..")

    def test_cd_no_such_file_or_directory_error(self):
        with self.assertRaises(ApplicationError):
            self.cd_app.exec(["nonexistent_directory"], [], self.std_out)

    def test_cd_not_a_directory_error(self):
        with self.assertRaises(ApplicationError):
            self.cd_app.exec(["file.txt"], [], self.std_out)

    # NOTE: causes eror whne running on docker unittest #######################
    def test_cd_permission_denied_error(self):
        # make permission_denied_dir
        os.mkdir("permission_denied_dir")
        # set permissions to deny access
        os.chmod("permission_denied_dir", 0o000)

        with self.assertRaises(ApplicationError):
            self.cd_app.exec(["permission_denied_dir"], [], self.std_out)

        # reset permissions
        os.chmod("permission_denied_dir", 0o777)


if __name__ == "__main__":
    unittest.main()
