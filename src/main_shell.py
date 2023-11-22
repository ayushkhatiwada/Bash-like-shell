"""
This file will replace shell.py 
This is start, where everything will be run from 
"""

import os
import sys

from collections import deque


def eval(cmd_line: str, stdout: deque[str]):
    # call the parsing and executing commands here

    pass


def process_input(cmd_line: str) -> None:

    # removes whitespace from beginning and end of string
    cmd_line = cmd_line.strip()

    # if user has not typed anything
    if not cmd_line:
        # return and print shell prompt again
        return

    stdout = deque()
    # errors caused when trying to parse and execute command will be handled below
    try:
        # eval functions modifies stdout deque defined above - pass by object reference
        eval(cmd_line, stdout)
    except:
        pass

    # final output of shell after everything has been done
    while stdout:
        print(stdout.popleft(), end="")


def exec_shell() -> None:
    num_of_args = len(sys.argv) - 1

    # non interactive mode - evaluating a single command once e.g. py shell.py -c "echo foo"
    if num_of_args > 0:
        
        if not (num_of_args == 2 and sys.argv[1] == "-c"):
            raise ValueError("""
                            Incorrect number of arguments passed
                            If you are trying to evaluate a single command once only
                            Try typing `-c "<command>"` with quotation marks
                            """)

    # interactive mode - REPL 
    else:
        while True:
            print(os.getcwd() + "> ", end="")
            cmd_line = input()
            process_input(cmd_line)


if __name__ == "__main__":
    exec_shell()
