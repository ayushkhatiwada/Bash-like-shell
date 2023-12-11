from singleton import Singleton
from applications.application_unsafe import ApplicationUnsafe
from applications.application import Application
from applications.application import ApplicationError

from applications.cat import Cat
from applications.cd import Cd
from applications.cut import Cut
from applications.echo import Echo
from applications.find import Find
from applications.grep import Grep
from applications.head import Head
from applications.ls import Ls
from applications.pwd import Pwd
from applications.sort import Sort
from applications.uniq import Uniq
from applications.tail import Tail


APPLICATIONS = {
    "cat": Cat,
    "cd": Cd,
    "cut": Cut,
    "echo": Echo,
    "find": Find,
    "grep": Grep,
    "head": Head,
    "ls": Ls,
    "pwd": Pwd,
    "sort": Sort,
    "uniq": Uniq,
    "tail": Tail
}


class ApplicationFactory(Singleton):
    """
    Singleton Application Factory.

    This factory class provides a centralized way to create instances of
    various applications. It ensures that only one instance of each
    application is created, making it more memory-efficient.

    Attributes:
        APPLICATIONS (dict): A dictionary mapping application names to their
        corresponding classes.
    """

    def get_application(self, application_name: str) -> Application:
        """
        Get an instance of the specified application.

        Args:
            application_name (str): The name of the application.

        Returns:
            Application: An instance of the specified application,
            either safe or unsafe depending on application name.

        Raises:
            ApplicationError: If the specified application is not found.
        """

        unsafe = False

        if application_name.startswith("_"):
            unsafe = True
            application_name = application_name[1:]

        if application_name not in APPLICATIONS:
            raise ApplicationError(f"{application_name}: command not found")

        if unsafe:
            return ApplicationUnsafe(APPLICATIONS[application_name]())
        else:
            return APPLICATIONS[application_name]()
