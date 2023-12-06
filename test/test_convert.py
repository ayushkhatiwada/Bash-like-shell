import unittest

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
            "echo hello", Command(Call((Argument("echo")), Atom(Argument("hello"))))
        )

    def test_ls_l_home(self):
        self.check_command(
            "ls -l /home",
            Command(
                Call((Argument("ls")), Atom(Argument("-l")), Atom(Argument("/home")))
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
                Call((Argument("echo")), Atom(Argument(Quoted(BackQuoted("date")))))
            ),
        )


if __name__ == "__main__":
    unittest.main()
