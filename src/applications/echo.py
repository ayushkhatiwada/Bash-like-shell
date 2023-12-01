from collections import deque

from .application import Application


class Echo(Application):
    name = "echo"

    def __init__(self) -> None:
        super().__init__()

    def exec(self, args: list[str], input: list[str], out: deque[str]) -> None:       
        output = " ".join(args)
        out.append(output + "\n")

# Todo (may): add flag -n to omit the new line
