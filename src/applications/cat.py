from abstract_application import AbstractApplication
from collections import deque
import os

class Cat(AbstractApplication):
    def exec(self, args: list[str], input: list[str], out: deque[str]) -> None:
        if args:
            for filename in args:
                if os.path.exists(filename):
                    with open(filename, 'r') as file:
                        for line in file:
                            out.append(line)
                else:
                    out.append(f"cat: {filename}: No such file or directory\n")
        else:
            out.extend(input)

    def help_message(self):
        return "cat [-n] [files...]"
