import unittest
from unittest.mock import Mock, patch
from collections import deque
import shell
from expressions import Call, Redirection, ApplicationError, ApplicationFactory

class TestCall(unittest.TestCase):
    def setUp(self):
        self.input_redirection_mock = Mock(spec=Redirection)
        self.input_redirection_mock.type = "<"
        self.input_redirection_mock.argument = "input.txt"

        call = Call()
        with patch('builtins.open', unittest.mock.mock_open(read_data='data')):
            with self.assertRaises(ApplicationError):
                call.handle_redirections([self.input_redirection_mock, self.input_redirection_mock])

        self.output_redirection_mock = Mock(spec=Redirection)
        self.output_redirection_mock.type = ">"
        self.output_redirection_mock.argument = "output.txt"

    def test_call_str(self):
        arg_mock = Mock()
        arg_mock.__str__ = Mock(return_value="ArgMock")
        call = Call(arg_mock)
        self.assertEqual(str(call), "Call(ArgMock)")


    def test_call_init(self):
        arg_mock = Mock()
        call = Call(arg_mock)
        self.assertEqual(call.args, (arg_mock,))

    def test_call_str(self):
        arg_mock = Mock()
        arg_mock.__str__ = Mock(return_value="ArgMock")
        call = Call(arg_mock)
        self.assertEqual(str(call), "Call(ArgMock)")

    def test_call_eq(self):
        arg_mock1 = Mock()
        arg_mock2 = Mock()
        call1 = Call(arg_mock1)
        call2 = Call(arg_mock1)
        call3 = Call(arg_mock2)
        self.assertEqual(call1, call2)
        self.assertNotEqual(call1, call3)


    def test_handle_output_redirection(self):
        output_redirection_mock = Mock(spec=Redirection)
        output_redirection_mock.type = ">"
        output_redirection_mock.argument = "output.txt"

        call = Call()
        input, output_file = call.handle_redirections([output_redirection_mock])

        self.assertEqual(output_file, "output.txt")
        self.assertEqual(input, [])

    def test_handle_multiple_output_redirections_error(self):
        call = Call()
        with self.assertRaises(ApplicationError):
            call.handle_redirections([self.output_redirection_mock, self.output_redirection_mock])

    def test_eval(self):
        app_mock = Mock()
        app_factory_mock = Mock(return_value=app_mock)
        arg_mock = Mock()
        arg_mock.eval.return_value = "arg"

        with patch.object(ApplicationFactory, 'get_application', app_factory_mock):
            call = Call(arg_mock)
            output = deque()
            call.eval(output)
            app_mock.exec.assert_called_once_with([], [], output)

    def test_eval_with_output_redirection(self):
        app_mock = Mock()
        app_factory_mock = Mock(return_value=app_mock)
        arg_mock = Mock()
        arg_mock.eval.return_value = "arg"

        with patch.object(ApplicationFactory, 'get_application', app_factory_mock):
            call = Call(arg_mock)
            output = deque()
            call.eval(output, input=deque())  # Removed output_file argument

    def test_eval_with_input_processing(self):
        app_mock = Mock()
        app_factory_mock = Mock(return_value=app_mock)

        command_mock = Mock()
        command_mock.eval.return_value = "some_command"

        with patch.object(ApplicationFactory, 'get_application', app_factory_mock):
            call = Call(command_mock)
            output = deque()
            input_data = deque(["line1\n", "line2\n"])
            call.eval(output, input=input_data)

    def test_eval_with_redirection_filtering(self):
        app_mock = Mock()
        app_factory_mock = Mock(return_value=app_mock)

        command_mock = Mock()
        command_mock.eval = Mock(return_value="some_command")

        redirection_mock = Mock(spec=Redirection)
        redirection_mock.type = "<"  # or ">" depending on the test case
        redirection_mock.argument = "file.txt"
        redirection_mock.eval.return_value = redirection_mock

        with patch.object(ApplicationFactory, 'get_application', app_factory_mock):
            with patch('builtins.open', unittest.mock.mock_open()):
                call = Call(command_mock, redirection_mock)
                output = deque()
                call.eval(output)

    def test_eval_with_file_write(self):
        app_mock = Mock()
        app_factory_mock = Mock(return_value=app_mock)

        command_mock = Mock()
        command_mock.eval = Mock(return_value="some_command")

        redirection_mock = Mock(spec=Redirection)
        redirection_mock.type = ">"
        redirection_mock.argument = "output.txt"
        redirection_mock.eval.return_value = redirection_mock

        app_output = deque(["output line 1\n", "output line 2\n"])

        with patch.object(ApplicationFactory, 'get_application', app_factory_mock):
            with patch('builtins.open', unittest.mock.mock_open()) as mock_file:
                call = Call(command_mock, redirection_mock)
                output = deque()
                app_mock.exec.side_effect = lambda *args, **kwargs: args[2].extend(app_output)
                call.eval(output)

                mock_file.assert_called_once_with("output.txt", "w")

                handle = mock_file()
                handle.write.assert_has_calls(
                    [unittest.mock.call("output line 1\n"), unittest.mock.call("output line 2\n")])

    def test_eval_with_output_redirection_to_file(self):
        app_mock = Mock()
        app_factory_mock = Mock(return_value=app_mock)

        command_mock = Mock()
        command_mock.eval.return_value = "some_command"

        redirection_mock = Mock(spec=Redirection)
        redirection_mock.type = ">"
        redirection_mock.eval.return_value = redirection_mock
        redirection_mock.argument = "output.txt"

        with patch.object(ApplicationFactory, 'get_application', app_factory_mock):
            call = Call(command_mock, redirection_mock)
            output = deque()

            with patch('builtins.open', unittest.mock.mock_open()) as mock_file:
                call.eval(output)
                mock_file.assert_called_once_with("output.txt", "w")
