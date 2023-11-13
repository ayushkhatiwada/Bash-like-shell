import os
from collections import deque
from typing import Deque

from abstract_application import AbstractApplication


class Pwd(AbstractApplication):
    """
    Prints the full filename of the current working directory
    """

    # out seems to be a double ended queue containing the current output
    def exec(self, out: Deque[str]) -> None:
        current_directory = os.getcwd()
        out.append(current_directory)
