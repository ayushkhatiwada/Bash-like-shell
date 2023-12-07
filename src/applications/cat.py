import os
from typing import Deque, List

from applications.application import Application


class Cat(Application):
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
                    with open(filename, 'r') as file:
                        # Read each line from the file and append to out
                        for line in file:
                            out.append(line)
                else:
                    # If the file does not exist, add an error message to out
                    out.append(f"Error: File '{filename}' not found.\n")
        else:
            # If there are no args, process the input list
            for line in input:
                out.append(line)
