import os
from typing import List, Deque

from .application import Application, ApplicationError


class Cd(Application):
    """Change th shell working directory."""

    name = "cd"

    def __init__(self) -> None:
        super().__init__()

    def exec(self, args: List[str], input: List[str], out: Deque[str]) -> None:
        if len(args) == 0:
            # if no args, do nothing
            return
        elif len(args) != 1:
            raise ApplicationError("cd: too many arguments")

        directory_path = args[0]
        try:
            os.chdir(directory_path)
        except FileNotFoundError:
            raise ApplicationError(
                f"cd: {directory_path}: No such file or directory.")
        except NotADirectoryError:
            raise ApplicationError(f"cd: {directory_path}: Not a directory.")
        except PermissionError:
            raise ApplicationError(f"cd: {directory_path}: Permission denied.")
