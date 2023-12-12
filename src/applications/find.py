import os
import fnmatch
from typing import List, Deque

from .application import Application, ArgumentError


class Find(Application):
    """
    find - search for files in a directory hierarchy
    """

    name = "find"

    def __init__(self) -> None:
        super().__init__()

    def exec(
        self,
        args: List[str],
        input: List[str],
        output: Deque[str]
    ) -> None:
        if len(args) not in [2, 3] or \
                args[0 if len(args) == 2 else 1] != "-name":
            raise ArgumentError(type(self), "find command must follow format: "
                                            "find [path] -name <pattern>")

        path = args[0] if len(args) == 3 else "."
        pattern = args[1] if len(args) == 2 else args[2]

        # walk through directory tree
        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    output.append(os.path.join(root, name) + "\n")
