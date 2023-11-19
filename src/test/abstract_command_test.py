import unittest
from collections import deque

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
