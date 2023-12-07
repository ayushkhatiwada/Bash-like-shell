from typing import Deque, List

from applications.application import Application


class Tail(Application):
    name = "tail"

    def __init__(self) -> None:
        super().__init__()

    def exec(self, args: List[str], input: List[str], out: Deque[str]) -> None:
        num_lines = 10  # Default number of lines
        file_name = None

        # Parsing command line arguments
        for arg in args:
            if arg.startswith("-n"):
                try:
                    num_lines = int(arg[2:])
                except ValueError:
                    raise ValueError("Invalid number of lines specified with -n option")
            else:
                file_name = arg

        # Reading lines from file or stdin
        lines = []
        if file_name:
            try:
                with open(file_name, 'r') as file:
                    lines = file.readlines()
            except FileNotFoundError:
                raise FileNotFoundError(f"File not found: {file_name}")
        else:
            lines = input

        # Outputting the last N lines
        for line in lines[-num_lines:]:
            out.append(line)
