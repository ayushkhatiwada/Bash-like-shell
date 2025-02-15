import os

# use this instead of list, and deque from collections
# fixes docker errors idk how
# it's because Dockerfile uses python 3.8
# and type hinting was done differently in 3.8 and below
# check Dockerfile
from typing import List, Deque

from .application import Application, ApplicationError


class Cat(Application):
    """
    cat - concatenate files and print on the standard output
    """

    name = "cat"

    def __init__(self) -> None:
        super().__init__()

    def exec(
        self,
        args: List[str],
        input: List[str],
        output: Deque[str]
    ) -> None:
        if args:
            # Process each file in the args
            for filename in args:
                # Check if the file exists
                if os.path.exists(filename):
                    # Open and read the file
                    with open(filename, "r") as file:
                        # Read each line from the file and append to out
                        for line in file:
                            output.append(line)
                else:
                    raise ApplicationError(f"File '{filename}' not found.")
        else:
            # If there are no args, process the input list
            for line in input:
                output.append(line + '\n')
