import os
from collections import deque
# from typing import Deque
# Use deque directly from collections instead of using Deque from typing library - See PEP 585 https://peps.python.org/pep-0585/

from abstract_application import AbstractApplication


class Pwd(AbstractApplication):
    """
    Prints the full filename of the current working directory
    """

    # out seems to be a double ended queue containing the current output

    # exec functions of commands don't need to return anything I think
    # instead they either modify the output deque, which will eventually be the output of a command
    # or in the case of cd, they use os.chdir
    def exec(self, args: list[str], input: list[str], out: deque[str]) -> None:
        current_directory = os.getcwd()
        out.append(current_directory + "\n")

