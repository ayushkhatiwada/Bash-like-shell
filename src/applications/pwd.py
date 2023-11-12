import os

from abstract_application import AbstractApplication


class Pwd(AbstractApplication):
    """
    Prints the full filename of the current working directory
    """

    def exec(self):
        current_directory = os.getcwd()
