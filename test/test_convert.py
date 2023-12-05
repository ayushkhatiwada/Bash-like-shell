import unittest
from antlr4 import InputStream, CommonTokenStream
from antlr.ShellGrammarLexer import ShellGrammarLexer
from antlr.ShellGrammarParser import ShellGrammarParser
from converter import Converter
from expressions import (
    Commmand,
    Call,
    Atom,
    Argument,
    Pipe,
    Seq,
    Redirection,
    Quoted,
    DoubleQuoted,
    BackQuoted,
)


class TestShellCommands(unittest.TestCase):
    def test_convert_check_command(self, command, expected_output):
        input_stream = InputStream(command)
        lexer = ShellGrammarLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(token_stream)
        parse_tree = parser.command()
        converter = Converter()
        actual_output = converter.visit(parse_tree)
        self.assertEqual(actual_output, expected_output)

    def test_convert_echo_hello(self):
        self.test_convert_check_command(
            "echo hello", Commmand(Call((Argument("echo")), Atom(Argument("hello"))))
        )

    def test_convert_ls_l_home(self):
        self.test_convert_check_command(
            "ls -l /home",
            Commmand(
                Call((Argument("ls")), Atom(Argument("-l")), Atom(Argument("/home")))
            ),
        )

    def test_convert_cat_file_txt_pipe_grep_search_term(self):
        self.test_convert_check_command(
            "cat file.txt | grep search_term",
            Commmand(
                Pipe(
                    Call((Argument("cat")), Atom(Argument("file.txt"))),
                    Call((Argument("grep")), Atom(Argument("search_term"))),
                )
            ),
        )

    def test_convert_echo_hello_redirection(self):
        self.test_convert_check_command(
            "echo hello > output.txt",
            Commmand(
                Call(
                    (Argument("echo")),
                    Atom(Argument("hello")),
                    Atom(Redirection(">", (Argument("output.txt")))),
                )
            ),
        )

    def test_convert_grep_search_term_redirection(self):
        self.test_convert_check_command(
            "grep search_term < input.txt",
            Commmand(
                Call(
                    (Argument("grep")),
                    Atom(Argument("search_term")),
                    Atom(Redirection("<", (Argument("input.txt")))),
                )
            ),
        )

    def test_convert_mkdir_cd_new_folder(self):
        self.test_convert_check_command(
            "mkdir new_folder; cd new_folder",
            Commmand(
                Seq(
                    Call((Argument("mkdir")), Atom(Argument("new_folder"))),
                    Call((Argument("cd")), Atom(Argument("new_folder"))),
                )
            ),
        )

    def test_convert_echo_double_quoted(self):
        self.test_convert_check_command(
            'echo "hello world"',
            Commmand(
                Call(
                    (Argument("echo")),
                    Atom(Argument(Quoted(DoubleQuoted("hello world")))),
                )
            ),
        )

    def test_convert_echo_back_quoted(self):
        self.test_convert_check_command(
            "echo `date`",
            Commmand(
                Call((Argument("echo")), Atom(Argument(Quoted(BackQuoted("date")))))
            ),
        )
