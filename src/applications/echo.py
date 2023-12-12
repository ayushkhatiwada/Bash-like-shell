from typing import List, Deque

from .application import Application


class Echo(Application):
    """
    echo — write arguments to standard output
    """

    name = "echo"

    def __init__(self) -> None:
        super().__init__()

    def exec(
        self,
        args: List[str],
        input: List[str],
        output: Deque[str]
    ) -> None:
        output.append(" ".join(input + args) + "\n")
