import os
# use this instead of list, and deque from collections
# fixes docker errors idk how
from typing import List, Deque

from .application import Application, ApplicationError


class Cat(Application):
    """
    cat - concatenate files and print on the standard output
    """

    name = "cat"

    def __init__(self) -> None:
        super().__init__()

    def exec(self, args: List[str], input: List[str], out: Deque[str]) -> None:
        if args:
            # Process each file in the args
            for filename in args:
                # Check if the file exists
                if os.path.exists(filename):
                    # Open and read the file
                    with open(filename, "r") as file:
                        # Read each line from the file and append to out
                        for line in file:
                            out.append(line)
                else:
                    raise ApplicationError(f"File '{filename}' not found.")
        else:
            # If there are no args, process the input list
            for line in input:
                out.append(line)
