import re
from typing import List, Deque

from .application import Application, ApplicationError


class Grep(Application):
    name = "grep"

    def exec(
        self,
        args: List[str],
        input: List[str],
        output: Deque[str]
    ) -> None:
        if not args:
            raise ApplicationError(f"{self.name}: No pattern provided.")

        pattern = args[0]
        files = args[1:]
        num_files = len(files)

        try:
            regex = re.compile(pattern)
        except re.error as e:
            raise ApplicationError(
                f"{self.name}: Invalid regular expression - {e}"
            )

        if files:
            # Process each file
            for file_name in files:
                try:
                    with open(file_name, 'r') as file:
                        for line in file:
                            if regex.search(line):
                                if num_files > 1:
                                    output.append(f"{file_name}:{line}")
                                else:
                                    output.append(line)
                except FileNotFoundError:
                    raise ApplicationError(
                        f"{self.name}: File not found: {file_name}"
                    )
        else:
            for line in input:
                if regex.search(line):
                    output.append(line + '\n')
