"""
This is the main shell file that will be executed when the user runs the shell.
"""

import os
import sys
from collections import deque
from typing import Deque

from antlr4 import CommonTokenStream, InputStream
from antlr.ShellGrammarLexer import ShellGrammarLexer
from antlr.ShellGrammarParser import ShellGrammarParser
from converter import Converter


def exec_shell() -> None:
    num_of_args = len(sys.argv) - 1

    # non interactive mode
    # evaluating a single command once e.g. py shell.py -c "echo foo"
    if num_of_args > 0:
        if not (num_of_args == 2 and sys.argv[1] == "-c"):
            raise ValueError(
                """
                Incorrect number of arguments passed
                If you are trying to evaluate a single command once only
                Try typing `-c "<command>"` with quotation marks
                """
            )

    # interactive mode - REPL
    else:
        while True:
            print(os.getcwd() + "> ", end="")
            cmd_line = input()
            process_input(cmd_line)


def process_input(cmd_line: str) -> None:
    # removes whitespace from beginning and end of string
    cmd_line = cmd_line.strip()

    # if no command was entered, do nothing
    if not cmd_line:
        return

    stdout = deque()
    # error handling for eval function
    # try:
    #     # pass stdout deque as reference
    #     eval(cmd_line, stdout)
    # except Exception as e:
    #     # TODO: add error handling
    #     print(f"An error occurred: {e}")
    eval(cmd_line, stdout)

    # final output of shell after everything has been done
    while stdout:
        print(stdout.popleft(), end="")


def eval(cmd_line: str, std_out: Deque[str]) -> None:
    # call the parsing and executing commands here
    expression = convert(cmd_line)
    expression.eval(output=std_out)


def convert(cmd_line: str):
    lexer = ShellGrammarLexer(InputStream(cmd_line))
    tokens = CommonTokenStream(lexer)
    parser = ShellGrammarParser(tokens)

    tree = parser.command()
    expression = tree.accept(Converter())

    return expression


if __name__ == "__main__":
    exec_shell()
