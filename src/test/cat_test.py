import unittest
from collections import deque
from applications.cat import Cat


class AbstractCommandTest(unittest.TestCase):
    """Abstract base class for testing command applications"""

    command_class = None 

    def setUp(self):
        self.command = self.command_class()

    def tearDown(self):
        del self.command

    def run_command(self, cmdline):
        out = deque()
        self.command.exec(cmdline, [], out)
        return out


class CatTest(AbstractCommandTest):
    """Class for testing the 'Cat' application"""

    command_class = Cat  # Set the command class for this test class

    def test_cat_file1_file2(self):
        result = self.run_command(["dir1/file1.txt", "dir1/file2.txt"])
        self.assertEqual(list(result), ["AAA", "BBB", "AAA", "CCC"])

    def test_cat_file_not_found(self):
        result = self.run_command(["nonexistent_file.txt"])
        self.assertEqual(list(result), ["Error: File 'nonexistent_file.txt' not found.\n"])

    # Add more test methods for different scenarios

if __name__ == "__main__":
    unittest.main()
