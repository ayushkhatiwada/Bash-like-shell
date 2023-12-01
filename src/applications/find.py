import os
import fnmatch
from collections import deque

from applications.application import Application


class Find(Application):
    name = "find"

    def __init__(self) -> None:
        super().__init__()

    def exec(self, args: list[str], input: list[str], out: deque[str]) -> None:
        # Parse arguments
        if '-name' not in args:
            raise ValueError("Missing -name argument in find command")

        name_index = args.index('-name')
        if name_index == len(args) - 1:
            raise ValueError("No pattern provided for -name in find command")

        pattern = args[name_index + 1]
        root_path = args[0] if args[0] != '-name' else '.'

        # Perform the search
        for path, dirs, files in os.walk(root_path):
            for file in files:
                if fnmatch.fnmatch(file, pattern):
                    out.append(os.path.join(path, file) + "\n")

# Add additional documentation or help messages as needed
