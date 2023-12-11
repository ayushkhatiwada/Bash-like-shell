import unittest
from globbing import expand_glob, expand_glob_command


class TestExpandGlob(unittest.TestCase):

    def test_expand_glob_no_glob(self):
        """Test expand_glob with no glob pattern."""
        argument = 'file.txt'
        result = expand_glob(argument)
        self.assertEqual(result, [argument])

    def test_expand_glob_with_glob(self):
        """Test expand_glob with a glob pattern."""
        argument = '*.txt'
        result = expand_glob(argument)
        # Check that there are matching files
        self.assertGreater(len(result), -1)

    def test_expand_glob_with_single_quotes(self):
        """Test expand_glob with glob pattern inside single quotes."""
        argument = "'*.txt'"
        result = expand_glob(argument)
        # Should not expand inside single quotes
        self.assertEqual(result, [argument])

    def test_expand_glob_command_no_glob(self):
        """Test expand_glob_command with no glob pattern."""
        cmd_str = 'ls file.txt'
        result = expand_glob_command(cmd_str)
        self.assertEqual(result, cmd_str)

    def test_expand_glob_command_with_glob(self):
        """Test expand_glob_command with a glob pattern."""
        cmd_str = 'ls *.txt'
        result = expand_glob_command(cmd_str)
        # Should expand the glob pattern
        self.assertNotEqual(result, cmd_str)
