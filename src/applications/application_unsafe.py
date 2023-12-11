from typing import Deque, List

from .application import Application


class ApplicationUnsafe(Application):
    """
    Unsafe Version of the Application
    Uses decorator design pattern to print error messages
    instead of raising exceptions.
    """

    def __init__(self, safe_application: Application) -> None:
        """
        Initialize the unsafe application with a safe application.

        Args:
            safe_application (Application): The safe application to be wrapped.
        """

        self.safe_application = safe_application

    def exec(
        self,
        args: List[str],
        input: List[str],
        output: Deque[str]
    ) -> None:
        """
        Execute the application command with error printing.

        Args:
            args (List[str]): List of command-line arguments.
            input (List[str]): List representing standard input.
            output (Deque[str]): Deque representing standard output.
        """

        try:
            self.safe_application.exec(args, input, output)
        except Exception as e:
            output.append(f"{e}\n")
