import os
from typing import Deque, List

from .application import Application, ApplicationError


class Ls(Application):
    """
    ls - list directory contents
    """

    name = 'ls'
    allowed_flags = {'-a', '-s', '-r'}

    def exec(
        self,
        args: List[str],
        input: List[str],
        output: Deque[str]
    ) -> None:
        args = input + args

        flags, args = self.parse_flags(
            args=args, allowed_flags=self.allowed_flags
        )

        # Determine the directory to list
        directory_path = args[0] if args else os.getcwd()

        try:
            # Get the list of files and directories in the specified path
            items = os.listdir(directory_path)
        except (FileNotFoundError, NotADirectoryError):
            raise ApplicationError(
                f"{self.name}: {directory_path}: No such file or directory."
            )

        # Filter out items that start with '.'
        visible_items = [
            item for item in items if not item.startswith('.')
        ]

        # Format the output
        formatted_output = '\t'.join(visible_items) + '\n'

        # Add the formatted output to the deque
        output.append(formatted_output)
