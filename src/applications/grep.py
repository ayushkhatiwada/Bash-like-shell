import re
from typing import List, Deque

from .application import Application, ApplicationError, ArgumentError


class Grep(Application):
    """
    Searches for lines containing a match to the specified pattern
    """

    name = "grep"

    def __init__(
        self,
        highlight_colour: str = "\u001b[35m",  # Magenta
        reset_colour: str = "\u001b[0m"  # White
    ):
        super().__init__()
        self.highlight_colour = highlight_colour
        self.reset_colour = reset_colour
        self.flags = {"-v": False, "-c": False}

    def exec(self, args: List[str], inp: List[str], out: Deque[str]):
        if not args:
            raise ArgumentError(type(self), "supply at least one argument")

        try:
            pattern = re.compile(args[0])
        except Exception:
            raise ApplicationError(f"'{args[0]}' is not a valid regex")

        if len(args) > 1:
            files = {
                file_name: read_lines(file_name) for file_name in args[1:]
            }
        else:
            files = {"": inp}

        for file_name, lines in files.items():
            for line in lines:

                if self.flags["-v"] ^ (not pattern.search(line)):
                    continue

                if self.flags["-c"]:
                    line = re.sub(
                        f"({pattern.pattern})",
                        f"{self.highlight_colour}\\g<1>{self.reset_colour}",
                        line
                    )

                if len(files) == 1:
                    out.append(line)
                else:
                    out.append(f"{file_name}:{line}")


def read_lines(file_name: str) -> List[str]:
    try:
        with open(file_name) as file:
            return file.read().splitlines(keepends=True)
    except FileNotFoundError:
        raise ApplicationError(f"file '{file_name}' does not exist")


# class Grep(Application):
#     name = "grep"

#     def exec(
#         self,
#         args: List[str],
#         input: List[str],
#         output: Deque[str]
#     ) -> None:
#         if not args:
#             raise ApplicationError(f"{self.name}: No pattern provided.")

#         pattern = args[0]
#         files = args[1:]

#         try:
#             regex = re.compile(pattern)
#         except re.error as e:
#             raise ApplicationError(
#                 f"{self.name}: Invalid regular expression - {e}"
#             )

#         if files:
#             # Process each file
#             for file_name in files:
#                 try:
#                     with open(file_name, 'r') as file:
#                         for line in file:
#                             if regex.search(line):
#                                 output.append(f"{file_name}:{line}")
#                 except FileNotFoundError:
#                     raise ApplicationError(
#                         f"{self.name}: File not found: {file_name}"
#                     )
#         else:
#             for line in input:
#                 if regex.search(line):
#                     output.append(line + '\n')
