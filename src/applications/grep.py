import os
import re
from collections import deque
from abstract_application import AbstractApplication

class Grep(AbstractApplication):
    
    def exec(self, args: list[str], input: list[str], out: deque[str]) -> None:
        if len(args) == 0:
            raise ValueError("No pattern provided for grep command")

        pattern = args[0]
        files = args[1:]

        # Compile the regular expression pattern
        try:
            regex = re.compile(pattern)
        except re.error:
            raise ValueError("Invalid regular expression")

        if files:
            # Process each file
            for file_name in files:
                try:
                    with open(file_name, 'r') as file:
                        for line in file:
                            if regex.search(line):
                                out.append(f"{file_name}:{line}")
                except FileNotFoundError:
                    raise FileNotFoundError(f"File not found: {file_name}")
        else:
            # Process stdin
            for line in input:
                if regex.search(line):
                    out.append(line)
