from abstract_application import AbstractApplication
from collections import deque
import os

class Cat():
    def exec(self, args: list[str], input: list[str], out: deque[str]) -> None:
        if args:
            # Process each file in the args
            for filename in args:
                try:
                    with open(filename, 'r') as file:
                        for line in file:
                            out.append(line)
                except FileNotFoundError:
                    out.append(f"Error: File '{filename}' not found.\n")
            else:
                # If there are no args, process the input list
                for line in input:
                    out.append(line)
