import sys
from typing import Deque, List

from .application import Application, ApplicationError

class Uniq(Application):
    name = 'uniq'

    def exec(
        self,
        args: List[str],
        input: List[str],
        output: Deque[str]
    ) -> None:
        ignore_case = '-i' in args
        file_path = None

        # Check for file argument
        for arg in args:
            if not arg.startswith('-'):
                file_path = arg
                break

        lines = []
        try:
            # Read from file or stdin
            if file_path:
                with open(file_path, 'r') as file:
                    lines = file.readlines()
            else:
                lines = input

            self.process_lines(lines, ignore_case, output)
        except FileNotFoundError:
            raise ApplicationError(
                f"{self.name}: {file_path}: No such file or directory."
            )
        except Exception as e:
            raise ApplicationError(str(e))

    def process_lines(
        self,
        lines: List[str],
        ignore_case: bool,
        output: Deque[str]
    ) -> None:
        if not lines:
            return

        previous_line = lines[0]
        output.append(previous_line)

        for line in lines[1:]:
            if ignore_case:
                if previous_line.strip().lower() != line.strip().lower():
                    output.append(line)
                    previous_line = line
            else:
                if previous_line.strip() != line.strip():
                    output.append(line)
                    previous_line = line
