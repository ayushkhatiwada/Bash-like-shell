from typing import Deque, List

from .application import Application, ApplicationError


class Head(Application):
    name = 'head'

    def exec(
        self,
        args: List[str],
        input: List[str],
        output: Deque[str]
    ) -> None:
        lines_to_print = 10

        # Process arguments
        for arg in args:
            if arg.startswith('-n'):
                try:
                    lines_to_print = int(arg[2:])
                except ValueError:
                    raise ApplicationError(
                        f"{self.name}: invalid number of lines: {arg[2:]}"
                    )
                args.remove(arg)
                break

        # Determine the file or stdin
        file_path = args[0] if args else None

        try:
            if file_path:
                with open(file_path, 'r') as file:
                    lines = file.readlines()
            else:
                lines = input
            lines = lines[:lines_to_print]

            formatted_output = ''.join(lines)

            output.append(formatted_output)

        except FileNotFoundError:
            raise ApplicationError(
                f"{self.name}: {file_path}: No such file or directory."
            )
        except Exception as e:
            raise ApplicationError(
                f"{self.name}: An error occurred: {str(e)}"
            )
