# import os
# import sys
from typing import Deque, List

from .application import Application, ApplicationError


class Cut(Application):
    name = 'cut'

    def exec(
        self,
        args: List[str],
        input: List[str],
        output: Deque[str]
    ) -> None:
        # Validate arguments
        if not args or len(args) < 2:
            raise ApplicationError(
                f"{self.name}: Missing required arguments."
            )

        option = args[0]
        if option != '-b':
            raise ApplicationError(
                f"{self.name}: Unsupported option {option}. Only -b is supported."
            )

        # Parse byte positions
        byte_positions = self.parse_byte_positions(args[1])

        # Determine the input source
        input_source = args[2] if len(args) > 2 else 'stdin'

        try:
            # Read from file or stdin
            if input_source == 'stdin':
                lines = input
            else:
                with open(input_source, 'r') as file:
                    lines = file.readlines()

            # Process each line
            for line in lines:
                selected_bytes = self.select_bytes(line, byte_positions)
                output.append(selected_bytes + '\n')

        except FileNotFoundError:
            raise ApplicationError(
                f"{self.name}: {input_source}: Unable to read file or input."
            )

    def parse_byte_positions(self, byte_str: str) -> List[slice]:
        byte_ranges = byte_str.split(',')
        slices = []
        for byte_range in byte_ranges:
            if '-' in byte_range:
                start, end = byte_range.split('-')
                start = int(start) - 1 if start else 0
                end = int(end) if end else None
                slices.append(slice(start, end))
            else:
                pos = int(byte_range) - 1
                slices.append(slice(pos, pos + 1))
        return slices

    def select_bytes(self, line: str, byte_positions: List[slice]) -> str:
        selected_bytes = []
        for position in byte_positions:
            selected_bytes.append(line[position])
        # Join the selected bytes and remove any trailing newline
        return ''.join(selected_bytes).rstrip('\n')


# from typing import List, Deque

# from .application import Application, ApplicationError, ArgumentError


# class Cut(Application):
#     name = "cut"

#     def __init__(self) -> None:
#         super().__init__()

#     def exec(self, args: List[str], input: List[str], out: Deque[str]) -> None:
#         if not args or args[0] != "-b":
#             raise ArgumentError("Invalid or missing -b option for cut command")

#         byte_ranges = self.parse_byte_ranges(args[1])
#         file_name = args[2] if len(args) > 2 else None

#         lines = self.read_lines(file_name, input)
#         for line in lines:
#             cut_line = self.extract_bytes(line, byte_ranges)
#             out.append(cut_line + '\n')

#     def parse_byte_ranges(self, byte_range_str: str) -> List[range]:
#         ranges = []
#         for part in byte_range_str.split(","):
#             if "-" in part:
#                 start, end = part.split("-")
#                 start = max(1, int(start)) if start else 1
#                 end = int(end) if end else None
#                 ranges.append(range(start - 1, end))
#             else:
#                 index = int(part) - 1
#                 ranges.append(range(index, index + 1))
#         return ranges

#     def read_lines(self, file_name: str, input: List[str]) -> List[str]:
#         if file_name:
#             try:
#                 with open(file_name, "r") as file:
#                     return file.readlines()
#             except FileNotFoundError:
#                 raise ApplicationError(f"File not found: {file_name}")
#         return input

#     def extract_bytes(self, line: str, byte_ranges: List[range]) -> str:
#         return "".join(
#             line[i] for r in byte_ranges for i in r if i < len(line)
#         )
