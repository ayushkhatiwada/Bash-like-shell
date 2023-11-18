from abc import ABC, abstractmethod

class AbstractApplication(ABC):
    """
    Abstract Application class

    Contains abstract exec function.
    Each command class (pwd, ls, cat, etc.) will inherit Application class and override the abstract exec function.

    Dynamic dispatch will then be used.
    """

    @abstractmethod
    def exec(self, cmdline, input, out):
        pass
