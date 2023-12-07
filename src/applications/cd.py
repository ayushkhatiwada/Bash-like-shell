import os
from typing import Deque, List

from applications.application import Application
from applications.application import ApplicationError


class Cd(Application):
    name = "cd"

    def __init__(self) -> None:
        super().__init__()

    def exec(self, args: List[str], input: List[str], out: Deque[str]) -> None:
        if len(args) != 1:
            raise ValueError(
                "Wrong number of command line arguments.\
                      cd takes exactly 1 argument."
            )

        directory_path = args[0]

        # Check if the directory_path is indeed a directory
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(
                f"{directory_path} is not a directory."
            )

        # Errors need to be changed for custom Application error
        try:
            os.chdir(directory_path)
        except FileNotFoundError:
            raise ApplicationError(
                f"{directory_path} directory does not exist."
            )
        except PermissionError:
            raise ApplicationError(
                f"Permission denied to access: {directory_path}."
            )
        except Exception as e:
            # General exception catch for any other unforeseen errors
            raise ApplicationError(
                f"An error occurred while changing directory: {e}."
            )
