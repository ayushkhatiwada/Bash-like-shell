from typing import Deque, List

from .application import Application, ApplicationError


class Sort(Application):
    """
    sort - sort lines of text files
    """

    name = "sort"
    allowed_flags = {"-r"}

    def exec(self, args: List[str], input: List[str], out: Deque[str]) -> None:
        flags, args = self.parse_flags(args, self.allowed_flags)

        # Separate options from potential file path
        file_path = None

        for arg in args:
            file_path = arg
            break

        # Determine the source of data (file or stdin)
        if file_path:
            try:
                with open(file_path, "r") as file:
                    lines = file.readlines()
            except FileNotFoundError:
                raise ApplicationError(
                    f"{self.name}: {file_path}: Unable to read file."
                )
        else:
            # Use stdin if no file is specified
            lines = [line + '\n' for line in input]

        reverse = "-r" in flags
        sorted_lines = sorted(lines, reverse=reverse)
        for line in sorted_lines:
            out.append(line)
