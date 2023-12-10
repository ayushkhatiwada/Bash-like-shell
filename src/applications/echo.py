from typing import List, Deque

from .application import Application


class Echo(Application):
    """
    echo — write arguments to standard output
    """

    name = "echo"

    def __init__(self) -> None:
        super().__init__()

    def exec(self, args: List[str], input: List[str], out: Deque[str]) -> None:
        output = " ".join(input + args)
        out.append(output + "\n")

# TODO (maybe): add flag -n to omit the new line
