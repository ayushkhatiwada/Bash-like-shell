import unittest
from collections import deque

from applications.echo import Echo


class TestEcho(unittest.TestCase):
    echo_app = Echo()

    def setUp(self):
        self.std_out = deque()

    def test_echo_single_word(self):
        self.echo_app.exec(["Hello"], [], self.std_out)
        self.assertEqual(self.std_out.pop(), "Hello\n")

    def test_echo_multiple_words(self):
        args = ["It's", "all", "about", "the", "customers"]
        ans = "It's all about the customers\n"
        self.echo_app.exec(args, [], self.std_out)
        self.assertEqual(self.std_out.pop(), ans)

    def test_echo_sentence(self):
        args = ["You say, The price of my love's not a price that you're..."]
        ans = "You say, The price of my love's not a price that you're...\n"
        self.echo_app.exec(args, [], self.std_out)
        self.assertEqual(self.std_out.pop(), ans)

    def test_echo_empty_string(self):
        self.echo_app.exec([""], [], self.std_out)
        self.assertEqual(self.std_out.pop(), "\n")

    # TODO (maybe): add tests for -n flag after flags have been implemented
