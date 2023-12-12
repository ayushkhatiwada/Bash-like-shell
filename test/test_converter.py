import unittest
from unittest.mock import Mock


from antlr4 import InputStream, CommonTokenStream
from antlr.ShellGrammarLexer import ShellGrammarLexer
from antlr.ShellGrammarParser import ShellGrammarParser

from converter import Converter
from expressions import (
    Command,
    Call,
    Atom,
    Argument,
    Pipe,
    Seq,
    Redirection,
    Quoted,
    DoubleQuoted,
    BackQuoted,
    SingleQuoted,
)


class TestShellCommands(unittest.TestCase):
    def check_command(self, command, expected_output):
        input_stream = InputStream(command)
        lexer = ShellGrammarLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(token_stream)
        parse_tree = parser.command()
        converter = Converter()
        actual_output = converter.visit(parse_tree)
        self.assertEqual(actual_output, expected_output)

    def test_echo_hello(self):
        self.check_command(
            "echo hello", Command(Call((Argument("echo")), Atom(
                Argument("hello"))))
        )

    def test_ls_l_home(self):
        self.check_command(
            "ls -l /home",
            Command(
                Call((Argument("ls")), Atom(Argument("-l")), Atom(
                    Argument("/home")))
            ),
        )

    def test_cat_file_txt_pipe_grep_search_term(self):
        self.check_command(
            "cat file.txt | grep search_term",
            Command(
                Pipe(
                    Call((Argument("cat")), Atom(Argument("file.txt"))),
                    Call((Argument("grep")), Atom(Argument("search_term"))),
                )
            ),
        )

    def test_echo_hello_redirection(self):
        self.check_command(
            "echo hello > output.txt",
            Command(
                Call(
                    (Argument("echo")),
                    Atom(Argument("hello")),
                    Atom(Redirection(">", (Argument("output.txt")))),
                )
            ),
        )

    def test_grep_search_term_redirection(self):
        self.check_command(
            "grep search_term < input.txt",
            Command(
                Call(
                    (Argument("grep")),
                    Atom(Argument("search_term")),
                    Atom(Redirection("<", (Argument("input.txt")))),
                )
            ),
        )

    def test_mkdir_cd_new_folder(self):
        self.check_command(
            "mkdir new_folder; cd new_folder",
            Command(
                Seq(
                    Call((Argument("mkdir")), Atom(Argument("new_folder"))),
                    Call((Argument("cd")), Atom(Argument("new_folder"))),
                )
            ),
        )

    def test_echo_double_quoted(self):
        self.check_command(
            'echo "hello world"',
            Command(
                Call(
                    (Argument("echo")),
                    Atom(Argument(Quoted(DoubleQuoted("hello world")))),
                )
            ),
        )

    def test_echo_back_quoted(self):
        self.check_command(
            "echo `date`",
            Command(
                Call((Argument("echo")), Atom(Argument(Quoted(
                    BackQuoted("date")))))
            ),
        )

    def test_echo_single_quoted(self):
        self.check_command(
            "echo 'hello world'",
            Command(
                Call(
                    Argument("echo"),
                    Atom(Argument(Quoted(SingleQuoted('hello', ' ', 'world'))))
                )
            )
        )

    def test_double_quoted_with_back_quoted(self):
        self.check_command(
            'echo "text before `date`"',
            Command(
                Call(
                    Argument("echo"),
                    Atom(
                        Argument(
                            Quoted(
                                DoubleQuoted(
                                    "text before ",
                                    BackQuoted("date")
                                )
                            )
                        )
                    )
                )
            )
        )

    def test_visitQuoted_with_invalid_context(self):
        mock_quoted_context = Mock(spec=ShellGrammarParser.QuotedContext)

        mock_quoted_context.children = [Mock()]

        converter = Converter()

        with self.assertRaises(AssertionError):
            converter.visitQuoted(mock_quoted_context)

    def test_visitRedirection_with_invalid_context(self):
        mock_redirection_context = Mock(
            spec=ShellGrammarParser.RedirectionContext
        )
        mock_redirection_context.children = [Mock()]

        converter = Converter()

        with self.assertRaises(AssertionError):
            converter.visitRedirection(mock_redirection_context)

    def test_visitSeq_with_invalid_context(self):
        mock_seq_context = Mock(spec=ShellGrammarParser.SeqContext)
        mock_seq_context.children = [Mock()]

        converter = Converter()

        with self.assertRaises(AssertionError):
            converter.visitSeq(mock_seq_context)

    def test_visitPipe_with_invalid_context(self):
        mock_pipe_context = Mock(spec=ShellGrammarParser.PipeContext)
        mock_pipe_context.children = [Mock(), Mock(), Mock()]

        converter = Converter()

        with self.assertRaises(TypeError):  # or another appropriate error
            converter.visitPipe(mock_pipe_context)

    def test_visitCommand_with_invalid_context(self):
        mock_command_context = Mock(spec=ShellGrammarParser.CommandContext)
        mock_command_context.children = [Mock()]

        converter = Converter()

        with self.assertRaises(AssertionError):
            converter.visitCommand(mock_command_context)

    def test_seq_with_call_on_left(self):
        self.check_command(
            "echo hello ; ls -l",
            Command(
                Seq(
                    Call(Argument("echo"), Atom(Argument("hello"))),
                    Call(Argument("ls"), Atom(Argument("-l")))
                )
            )
        )

    def test_seq_with_pipe_on_right(self):
        self.check_command(
            "ls -l ; grep pattern | sort",
            Command(
                Seq(
                    Call(Argument("ls"), Atom(Argument("-l"))),
                    Pipe(
                        Call(Argument("grep"), Atom(Argument("pattern"))),
                        Call(Argument("sort"))
                    )
                )
            )
        )

    def test_seq_with_pipe_on_left(self):
        self.check_command(
            "cat file.txt | grep pattern ; ls -l",
            Command(
                Seq(
                    Pipe(
                        Call(Argument("cat"), Atom(Argument("file.txt"))),
                        Call(Argument("grep"), Atom(Argument("pattern")))
                    ),
                    Call(Argument("ls"), Atom(Argument("-l")))
                )
            )
        )

    def test_seq_with_nested_seq_on_right(self):
        self.check_command(
            "echo start ; echo middle ; echo end",
            Command(
                Seq(
                    Call(Argument("echo"), Atom(Argument("start"))),
                    Seq(
                        Call(Argument("echo"), Atom(Argument("middle"))),
                        Call(Argument("echo"), Atom(Argument("end")))
                    )
                )
            )
        )

    def test_seq_with_invalid_right(self):
        with self.assertRaises(AssertionError):
            self.check_command("echo hello ; invalid_command", None)

    def test_pipe_with_right_side_pipe(self):
        self.check_command(
            "cat file.txt | grep pattern | sort",
            Command(
                Pipe(
                    Call(Argument("cat"), Atom(Argument("file.txt"))),
                    Pipe(
                        Call(Argument("grep"), Atom(Argument("pattern"))),
                        Call(Argument("sort"))
                    )
                )
            )
        )

    def test_call_with_direct_redirection(self):
        self.check_command(
            "command > output.txt",
            Command(
                Call(
                    Argument("command"),
                    Atom(Redirection(">", Argument("output.txt")))
                )
            )
        )
