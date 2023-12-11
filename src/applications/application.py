from abc import ABC, abstractmethod
from typing import Deque, List, Set, Tuple


class Application(ABC):
    """
    Abstract Application class.

    Contains abstract execute function.
    Each command class (pwd, ls, cat, etc.) will inherit from Application.
    Each child class will override the abstract execute function.

    Dynamic dispatch will then be used.
    """

    name: str
    allowed_flags: Set[str]

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
            FlagError: Raised if a flag error occurs.
            ApplicationError: Raised if an application error occurs.
        """

        pass

    @staticmethod
    def parse_flags(
        args: List[str],
        allowed_flags: Set[str]
    ) -> Tuple[Set[str], List[str]]:
        """
        Parse flags, and clean arguments.

        Args:
            args (List[str]): List of command-line arguments.
            allowed_flags (Set[str]): Set of allowed flags.

        Returns:
            Tuple[Set[str], List[str]]: A tuple containing the parsed flags and
            cleaned arguments.

        Raises:
            FlagError: Raised if a flag error occurs.
        """

        flags = set()
        clean_args = []

        for arg in args:
            if arg.startswith('-'):
                if arg not in allowed_flags:
                    raise FlagError(f"Invalid flag: {arg}")
                flags.add(arg)
            else:
                clean_args.append(arg)

        return flags, clean_args


class ArgumentError(Exception):
    """Raised if an argument error occurs"""


class FlagError(Exception):
    """Raised if a flag error occurs"""


class ApplicationError(Exception):
    """Raised if an application errors occur"""
