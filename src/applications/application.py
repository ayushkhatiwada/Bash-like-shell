from abc import ABC, abstractmethod
from typing import Deque, List


class Application(ABC):
    """
    Abstract Application class.

    Contains abstract execute function.
    Each command class (pwd, ls, cat, etc.) will inherit from Application.
    Each child class will override the abstract execute function.

    Dynamic dispatch will then be used.
    """

    name: str

    @abstractmethod
    def exec(
        self,
        args: List[str],
        input: List[str],
        output: Deque[str]
    ) -> None:
        """
        Execute the application command.

        Args:
            args (List[str]): List of command-line arguments.
            input (List[str]): List representing standard input.
            output (Deque[str]): Deque representing standard output.

        Raises:
            ArgumentError: Raised if an argument error occurs.
            ApplicationError: Raised if an application error occurs.
        """

        pass


class ArgumentError(Exception):
    """Raised if an argument error occurs"""


class ApplicationError(Exception):
    """Raised if an application errors occur"""
