from typing import Deque, List

from .application import Application, ApplicationError

"""
    def test_cut_overlapping(self):
        cmdline = "cut -b 2-,3- dir1/file1.txt"
        stdout = self.eval(cmdline)
        result = stdout.strip().split("\n")
        self.assertEqual(result, ["AA", "BB", "AA"])

Need to pass this specific test case from system_test/tests.py
"""


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
                f"{self.name}: Unsupported option {option}. "
                f"Only -b is supported."
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
        byte_indices = set()
        for position in byte_positions:
            start = position.start if position.start is not None else 0
            stop = position.stop if position.stop is not None else len(line)
            byte_indices.update(range(start, stop))

        selected_bytes = [
            line[i] for i in sorted(byte_indices) if i < len(line)
        ]
        return ''.join(selected_bytes).rstrip('\n')
