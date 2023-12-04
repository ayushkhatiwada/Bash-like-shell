from collections import deque
from .application import Application, ApplicationError

class Head(Application):
    name = "head"

    def __init__(self):
        super().__init__()

    def exec(self, args: list[str], input: list[str], out: deque[str]) -> None:
        num_lines = 10  # Default number of lines
        file_name = None

        # Parsing command line arguments
        for arg in args:
            if arg.startswith("-n"):
                try:
                    num_lines = int(arg[2:])
                except ValueError:
                    raise ApplicationError(
                        f"{self.name}: Invalid number of lines specified with -n option"
                    )
            else:
                file_name = arg

        # Reading lines from file or stdin
        lines = []
        if file_name:
            try:
                with open(file_name, 'r') as file:
                    for _ in range(num_lines):
                        line = file.readline()
                        if not line:
                            break
                        lines.append(line)
            except FileNotFoundError:
                raise ApplicationError(f"{self.name}: File not found: {file_name}")
        else:
            lines = input[:num_lines]

        # Outputting lines
        formatted_output = ''.join(lines)
        out.append(formatted_output)
