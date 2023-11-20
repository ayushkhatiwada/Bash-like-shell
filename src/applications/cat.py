import os
# import sys
# sys.path.append('/com.docker.devenvironments.code/src')
from collections import deque

from .abstract_application import AbstractApplication


class Cat(AbstractApplication):
    def __init__(self) -> None:
        super().__init__()

    def exec(self, args: list[str], input: list[str], out: deque[str]) -> None:
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
