from typing import Deque, List

from .application import Application


class ApplicationUnsafe(Application):
    """
    Unsafe Version of the Application
    Uses decorator design pattern to print error messages
    instead of raising exceptions.
    """

    def __init__(self, safe_application: Application) -> None:
        """Initialize the unsafe application with a safe application."""
        self.safe_application = safe_application

    def exec(
        self,
        args: List[str],
        input: List[str],
        output: Deque[str]
    ) -> None:
        try:
            self.safe_application.exec(args, input, output)
        except Exception as e:
            output.append(f"{e}\n")
