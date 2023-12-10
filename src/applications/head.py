from typing import Deque, List

from .application import Application, ApplicationError


class Head(Application):
    name = 'head'
    allowed_flags = {'-n'}

    def exec(
        self,
        args: List[str],
        input: List[str],
        output: Deque[str]
    ) -> None:
        flags, args = self.parse_flags(
            args=args, allowed_flags=self.allowed_flags
        )

        lines_to_print = 10

        if '-n' in flags:
            try:
                lines_to_print = int(args[0])
            except ValueError:
                raise ApplicationError(
                    f"{self.name}: invalid number of lines: {args[0]}"
                )
            args.remove(args[0])

        # # Process arguments
        # for arg in args:
        #     if arg.startswith('-n'):
        #         try:
        #             lines_to_print = int(arg[2:])
        #         except ValueError:
        #             raise ApplicationError(
        #                 f"{self.name}: invalid number of lines: {arg[2:]}"
        #             )
        #         args.remove(arg)
        #         break

        # Determine the file or stdin
        file_path = args[0] if args else None

        try:
            if file_path:
                with open(file_path, 'r') as file:
                    lines = file.readlines()
            else:
                lines = [line + '\n' for line in input]
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
