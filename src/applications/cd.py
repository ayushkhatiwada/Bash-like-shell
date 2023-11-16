import os
from collections import deque

from abstract_application import AbstractApplication


class Cd(AbstractApplication):

    def exec(self, args: list[str], input: list[str], out: deque[str]) -> None:
        if len(args) != 1:
            raise ValueError("wrong number of command line arguments. cd takes exactly 1 argument")
        
        directory_path = args[0]

        try:
            os.chdir(directory_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"{directory_path} directory does not exist")
        except PermissionError:
            raise PermissionError(f"Permission denied to access: {directory_path}")
        except NotADirectoryError:
            raise NotADirectoryError(f"{directory_path} Not a directory")

            # if not os.path.isdir(directory_path):
