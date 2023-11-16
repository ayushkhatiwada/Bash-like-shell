from collections import deque

from abstract_application import AbstractApplication


class Echo(AbstractApplication):
    
    def exec(self, args: list[str], input: list[str], out: deque[str]) -> None:       
        output = " ".join(args)
        out.append(output + "\n")

# To may do: add flag -n to omit the new line
