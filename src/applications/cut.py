from typing import List, Deque

from .application import Application, ApplicationError, ArgumentError


class Cut(Application):
    name = "cut"

    def __init__(self) -> None:
        super().__init__()

    def exec(self, args: List[str], input: List[str], out: Deque[str]) -> None:
        if not args or args[0] != "-b":
            raise ArgumentError("Invalid or missing -b option for cut command")

        byte_ranges = self.parse_byte_ranges(args[1])
        file_name = args[2] if len(args) > 2 else None

        lines = self.read_lines(file_name, input)
        for line in lines:
            cut_line = self.extract_bytes(line, byte_ranges)
            out.append(cut_line + '\n')

    def parse_byte_ranges(self, byte_range_str: str) -> List[range]:
        ranges = []
        for part in byte_range_str.split(","):
            if "-" in part:
                start, end = part.split("-")
                start = max(1, int(start)) if start else 1
                end = int(end) if end else None
                ranges.append(range(start - 1, end))
            else:
                index = int(part) - 1
                ranges.append(range(index, index + 1))
        return ranges

    def read_lines(self, file_name: str, input: List[str]) -> List[str]:
        if file_name:
            try:
                with open(file_name, "r") as file:
                    return file.readlines()
            except FileNotFoundError:
                raise ApplicationError(f"File not found: {file_name}")
        return input

    def extract_bytes(self, line: str, byte_ranges: List[range]) -> str:
        return "".join(
            line[i] for r in byte_ranges for i in r if i < len(line)
        )


# Add additional documentation or help messages as needed
