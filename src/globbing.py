from glob import glob
from shlex import split


def expand_glob(argument):
    # if * inside single quotes, don't expand
    if (
        '*' not in argument or
        argument[0] == '\'' and argument[-1] == '\''
    ):
        return [argument]
    else:
        matching_files = glob(argument)
        return matching_files


def expand_glob_command(cmd_str):
    if '*' not in cmd_str:
        return cmd_str

    arguments = split(cmd_str, posix=False)
    expanded_arguments = []

    for arg in arguments:
        expanded_args = expand_glob(arg)
        expanded_arguments.extend(expanded_args)

    # join the expanded arguments into a single string
    expanded_command = ' '.join(expanded_arguments)
    return expanded_command
