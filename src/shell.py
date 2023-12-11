import os
import sys
from collections import deque
from typing import Deque

from antlr4 import CommonTokenStream, InputStream
from antlr.ShellGrammarLexer import ShellGrammarLexer
from antlr.ShellGrammarParser import ShellGrammarParser

import converter
from applications.application import ApplicationError, FlagError, ArgumentError
from globbing import expand_glob_command


def exec_shell() -> None:
    """
    Execute the shell in either non-interactive or interactive mode.

    Non-Interactive Mode:
    - Evaluates a single command passed as a command-line argument
      (e.g., `py shell.py -c "echo foo"`).

    Interactive Mode (REPL):
    - Prompts the user for input continuously until interrupted.

    Raises:
        ValueError: If the number of command-line arguments is incorrect
                    in non-interactive mode.
    """

    num_args = len(sys.argv) - 1

    # non interactive mode
    if num_args > 0:
        if not (num_args == 2 and sys.argv[1] == "-c"):
            raise ValueError(
                """
                Incorrect number of arguments passed
                If you are trying to evaluate a single command once only
                Try typing `-c "<command>"` with quotation marks
                """
            )
        cmd_line = sys.argv[2]
        process_input(cmd_line)

    # interactive mode (REPL)
    else:
        while True:
            print(os.getcwd() + "> ", end="")
            cmd_line = input()
            process_input(cmd_line)


def process_input(cmd_line: str) -> None:
    """
    Process the user input, expanding globbing, and executing the command.

    Args:
        cmd_line (str): The user input command.
    """

    cmd_line = cmd_line.strip()  # remove leading and trailing whitespaces
    cmd_line = expand_glob_command(cmd_line)  # expand globbing

    if not cmd_line:
        return

    std_out = deque()
    try:
        eval(cmd_line, std_out)
    except ArgumentError as err:
        sys.stderr.write(f"argument error: {err}\n")
    except FlagError as err:
        sys.stderr.write(f"flag error: {err}\n")
    except ApplicationError as err:
        sys.stderr.write(f"application error: {err}\n")

    # output to stdout after command execution
    while std_out:
        print(std_out.popleft(), end="")


def eval(cmd_line: str, std_out: Deque[str]) -> None:
    """
    Evaluate the command by converting it into an expression and executing it.

    Args:
        cmd_line (str): The user input command.
        std_out (Deque[str]): The deque representing standard output.
    """

    expression = convert(cmd_line)
    expression.eval(output=std_out)


def convert(cmd_line: str):
    """
    Convert the command string into an expression.

    Args:
        cmd_line (str): The user input command.

    Returns:
        Expression: The converted expression.
    """

    lexer = ShellGrammarLexer(InputStream(cmd_line))
    tokens = CommonTokenStream(lexer)
    parser = ShellGrammarParser(tokens)

    tree = parser.command()
    expression = tree.accept(converter.Converter())

    return expression


if __name__ == "__main__":
    exec_shell()
