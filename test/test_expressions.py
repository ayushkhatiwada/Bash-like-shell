import unittest
from expressions import (
    Command,
    Pipe,
    Seq,
    Call,
    Atom,
    Redirection,
    Argument,
    Quoted,
    SingleQuoted,
    DoubleQuoted,
    BackQuoted,
)


class TestShellFeatures(unittest.TestCase):
    def test_command(self):
        cmd = Command(Call(Argument("echo")))
        self.assertEqual(str(cmd), "Command(Call(Argument(echo)))")

    def test_pipe(self):
        left = Call(Argument("ls"))
        right = Call(Argument("grep"), Atom(Argument("pattern")))
        pipe = Pipe(left, right)

        self.assertEqual(
            str(pipe),
            "Pipe(Call(Argument(ls)), "
            "Call(Argument(grep), Atom(Argument(pattern))))"
        )

    def test_seq(self):
        left = Call(Argument("echo"), Atom(Argument("hello")))
        right = Call(Argument("wc"))
        seq = Seq(left, right)

        self.assertEqual(
            str(seq),
            "Seq(Call(Argument(echo), Atom(Argument(hello))), "
            "Call(Argument(wc)))"
        )

    def test_call(self):
        call = Call(Argument("echo"), Atom(Argument("hello")))
        self.assertEqual(
            str(call),
            "Call(Argument(echo), Atom(Argument(hello)))"
        )

    def test_atom(self):
        atom = Atom(Argument("echo"))
        self.assertEqual(
            str(atom),
            "Atom(Argument(echo))"
        )

    def test_redirection(self):
        redirection = Redirection(">", Atom(Argument("output.txt")))
        self.assertEqual(
            str(redirection),
            "Redirection(>, Atom(Argument(output.txt)))"
        )

    def test_argument(self):
        argument = Argument(Quoted(DoubleQuoted(["hello", "world"])))
        self.assertEqual(
            str(argument),
            "Argument(Quoted(DoubleQuoted(['hello', 'world'])))"
        )

    def test_quoted(self):
        quoted = Quoted(SingleQuoted("single_quoted"))
        self.assertEqual(
            str(quoted),
            "Quoted(SingleQuoted(single_quoted))"
        )

    def test_single_quoted(self):
        single_quoted = SingleQuoted("single_quoted")
        self.assertEqual(
            str(single_quoted),
            "SingleQuoted(single_quoted)"
        )

    def test_double_quoted(self):
        double_quoted = DoubleQuoted(["hello", "world"])
        self.assertEqual(
            str(double_quoted),
            "DoubleQuoted(['hello', 'world'])"
        )

    def test_back_quoted(self):
        back_quoted = BackQuoted(Atom(Argument("command")))
        self.assertEqual(
            str(back_quoted),
            "BackQuoted(Atom(Argument(command)))"
        )
