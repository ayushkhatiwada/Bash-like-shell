import os
from typing import Deque, List

from .application import Application


class Pwd(Application):
    """
    pwd - print name of current/working directory
    """

    name = 'pwd'

    def exec(
        self,
        args: List[str],
        input: List[str],
        output: Deque[str]
    ) -> None:
        # Get the current working directory
        current_directory = os.getcwd()

        # Format the output with a newline
        formatted_output = current_directory + '\n'

        # Add the formatted output to the deque
        output.append(formatted_output)
