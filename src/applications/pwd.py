import os
from collections import deque

from .application import Application


class Pwd(Application):
    """
    Prints the full filename of the current working directory
    """

    name = "pwd"

    def __init__(self) -> None:
        super().__init__()

    # out seems to be a double ended queue containing the current output

    # exec functions of commands don't need to return anything I think
    # instead they either modify the output deque
    #   - which will eventually be the output of a command
    # or in the case of cd, they use os.chdir
    def exec(self, args: list[str], input: list[str], out: deque[str]) -> None:
        current_directory = os.getcwd()
        out.append(current_directory + "\n")
