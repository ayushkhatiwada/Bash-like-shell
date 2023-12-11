import unittest
from unittest.mock import patch
from io import StringIO
from shell import exec_shell, process_input
from applications.application import ArgumentError, FlagError, ApplicationError
import os


class TestShell(unittest.TestCase):
    @patch('sys.argv', new=['shell.py', '-c', 'echo foo'])
    def test_exec_shell_non_interactive(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            exec_shell()
        self.assertIn("foo", mock_stdout.getvalue())

    def test_exec_shell_value_error(self):
        with patch('sys.argv', new=['shell.py', '-c']), \
             self.assertRaises(ValueError) as context:
            exec_shell()
        self.assertIn(
            "Incorrect number of arguments passed",
            str(context.exception)
        )

    def test_process_input_empty_command(self):
        with patch('builtins.input', side_effect=["", "exit"]), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            process_input("")
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('builtins.input', side_effect=["echo test", "exit"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_process_input_non_empty_command(self, mock_stdout, mock_input):
        process_input("echo test")
        self.assertEqual(mock_stdout.getvalue().strip(), "test")

    @patch('shell.eval')
    def test_process_input_argument_error(self, mock_eval):
        mock_eval.side_effect = ArgumentError("Test ArgumentError")
        with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            process_input("some_command")
        self.assertIn("argument error: Test ArgumentError", mock_stderr.getvalue())

    @patch('shell.eval')
    def test_process_input_flag_error(self, mock_eval):
        mock_eval.side_effect = FlagError("Test FlagError")
        with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            process_input("some_command")
        self.assertIn("flag error: Test FlagError", mock_stderr.getvalue())

    @patch('shell.eval')
    def test_process_input_application_error(self, mock_eval):
        mock_eval.side_effect = ApplicationError("Test ApplicationError")
        with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            process_input("some_command")
        self.assertIn("application error: Test ApplicationError", mock_stderr.getvalue())

    @patch('builtins.input', side_effect=["echo test", KeyboardInterrupt])
    @patch('sys.stdout', new_callable=StringIO)
    def test_interactive_mode_loop(self, mock_stdout, mock_input):
        with patch('sys.argv', new=['shell.py']):
            with self.assertRaises(KeyboardInterrupt):
                exec_shell()
        output = mock_stdout.getvalue()
        self.assertIn(os.getcwd() + "> ", output)
        self.assertIn("test", output)
