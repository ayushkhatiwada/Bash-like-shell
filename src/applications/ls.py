import os
from collections import deque

from abstract_application import AbstractApplication


class Ls(AbstractApplication):

    def exec(self, args: list[str], input: list[str], out: deque[str]) -> None:
        
        # not correct as ls can list the contents of multiple directories 
        # but this may be good enough for this cwk
        if len(args) > 1:
            raise ValueError("wrong number of command line arguments")
        
        directory_path = os.getcwd() if len(args) == 0 else args[0]

        try:
            files = os.listdir(directory_path)
        except NotADirectoryError:
            raise NotADirectoryError(f"{directory_path} Not a directory")

        if len(files):
            out.append("\t".join(files) + "\n")
