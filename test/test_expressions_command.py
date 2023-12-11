import unittest
from unittest.mock import Mock
from collections import deque
import shell
from expressions import Command  # Replace with your actual module import

class TestCommand(unittest.TestCase):
    def test_command_init(self):
        child_mock = Mock()
        cmd = Command(child_mock)
        self.assertEqual(cmd.child, child_mock)

    def test_command_str(self):
        child_mock = Mock()
        child_mock.__str__ = Mock(return_value="MockChild")
        cmd = Command(child_mock)
        self.assertEqual(str(cmd), "Command(MockChild)")

    def test_command_eq(self):
        child_mock1 = Mock()
        child_mock2 = Mock()
        cmd1 = Command(child_mock1)
        cmd2 = Command(child_mock1)
        cmd3 = Command(child_mock2)
        self.assertEqual(cmd1, cmd2)
        self.assertNotEqual(cmd1, cmd3)

    def test_command_eval(self):
        child_mock = Mock()
        cmd = Command(child_mock)
        output = deque()
        cmd.eval(output)
        child_mock.eval.assert_called_once_with(output)
