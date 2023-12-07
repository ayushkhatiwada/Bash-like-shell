from typing import Deque, List

from applications.application import Application


class Echo(Application):
    name = "echo"

    def __init__(self) -> None:
        super().__init__()

    def exec(self, args: List[str], input: List[str], out: Deque[str]) -> None:
        output = " ".join(args)
        out.append(output + "\n")

# To do (may): add flag -n to omit the new line
