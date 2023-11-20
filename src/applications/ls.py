import os
from collections import deque

from abstract_application import AbstractApplication


class Ls(AbstractApplication):
    
    name = "ls"

    def __init__(self) -> None:
        super().__init__()

    def exec(self, args: list[str], input: list[str], out: deque[str]) -> None:
        # Determine the directory to list
        directory_path = args[0] if args else os.getcwd()

        try:
            # Get the list of files and directories in the specified path
            items = os.listdir(directory_path)

            # Filter out items that start with '.'
            visible_items = [item for item in items if not item.startswith('.')]

            # Format the output
            formatted_output = '\t'.join(visible_items) + '\n'

            # Add the formatted output to the deque
            out.append(formatted_output)
        except FileNotFoundError:
            raise FileNotFoundError(f"The directory {directory_path} does not exist.")
        except PermissionError:
            raise PermissionError(f"Permission denied to access: {directory_path}.")
        except NotADirectoryError:
            raise NotADirectoryError(f"{directory_path} is not a directory.")
        except Exception as e:
            # General exception catch for any other unforeseen errors
            raise Exception(f"An error occurred: {e}.")
