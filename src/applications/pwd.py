import os


class Pwd():
    """
    Prints the full filename of the current working directory
    """

    def run(self):
        current_directory = os.getcwd()
