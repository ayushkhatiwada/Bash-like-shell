from abstract_application import AbstractApplication
from collections import deque


class Echo(AbstractApplication):
    
    def exec(self, args: list[str], input: list[str], out: deque[str]) -> None:       
        pass
