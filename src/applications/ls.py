import os
from typing import Deque, List

from .application import Application, ApplicationError


class Ls(Application):
    name = 'ls'

    def exec(
        self,
        args: List[str],
        input: List[str],
        output: Deque[str]
    ) -> None:
        # Determine the directory to list
        directory_path = args[0] if args else os.getcwd()

        try:
            # Get the list of files and directories in the specified path
            items = os.listdir(directory_path)

            # Filter out items that start with '.'
            visible_items = [
                item for item in items if not item.startswith('.')
            ]

            # Format the output
            formatted_output = '\t'.join(visible_items) + '\n'

            # Add the formatted output to the deque
            output.append(formatted_output)
        except (FileNotFoundError, NotADirectoryError):
            raise ApplicationError(
                f"{self.name}: {directory_path}: No such file or directory."
            )
        except Exception as e:
            # General exception catch for any other unforeseen errors
            raise ApplicationError(f"An error occurred: {e}.")
