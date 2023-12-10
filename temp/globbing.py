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


if __name__ == "__main__":
    cmd_strs = [
        "echo *.txt",
        "echo temp/*.txt",
        'echo "a  b"',
        "find requirements.txt -name \'*.txt\'",
        'echo "a `echo "b"`"',
        "find dir1 -name \'*.txt\'",
    ]

    for cmd_str in cmd_strs:
        expanded = expand_glob_command(cmd_str)
        # print(cmd_str == expanded)
        print(cmd_str)
        print(expanded)
        print("Equal?:", cmd_str == expanded)

        print()

    # print(expand_glob("echo"))

    # assert cmd_str == expanded
