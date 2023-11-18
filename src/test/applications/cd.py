import os
from collections import deque
from abstract_application import AbstractApplication

class Cd(AbstractApplication):
    def exec(self, args: list[str], input: list[str], out: deque[str]) -> None:
        if len(args) != 1:
            raise ValueError("Wrong number of command line arguments. cd takes exactly 1 argument.")

        directory_path = args[0]

        # Check if the directory_path is indeed a directory
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"{directory_path} is not a directory.")

        try:
            os.chdir(directory_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"{directory_path} directory does not exist.")
        except PermissionError:
            raise PermissionError(f"Permission denied to access: {directory_path}.")
        except Exception as e:
            # General exception catch for any other unforeseen errors
            raise Exception(f"An error occurred while changing directory: {e}.")
