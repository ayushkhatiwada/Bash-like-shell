import re
from typing import List, Deque

from .application import Application, ApplicationError


class Grep(Application):
    name = "grep"

    def exec(self, args: List[str], inp: List[str], out: Deque[str]) -> None:
        if not args:
            raise ApplicationError(f"{self.name}: No pattern provided.")

        pattern = args[0]
        files = args[1:]

        try:
            regex = re.compile(pattern)
        except re.error as e:
            error_msg = f"{self.name}: Invalid regular expression - {e}"
            raise ApplicationError(error_msg)

        if files:
            # Process each file
            for file_name in files:
                try:
                    with open(file_name, 'r') as file:
                        for line in file:
                            if regex.search(line):
                                out.append(f"{file_name}:{line}")
                except FileNotFoundError:
                    error_msg = f"{self.name}: File not found: {file_name}"
                    raise ApplicationError(error_msg)
        else:
            for line in inp:
                if regex.search(line):
                    out.append(line)
