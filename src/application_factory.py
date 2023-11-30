from singleton import Singleton
from applications.abstract_application import AbstractApplication
from custom_exceptions import ApplicationError

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


# dictionary used to avoid if/ swtich statements, see below 
# APPLICATION_DICT = { application.name: application for application in [Cat, Cd, Cut, Echo, Find, Grep, Head, Ls, Pwd, Sort, Uniq, Tail] }
APPLICATION_DICT = {
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
    Singleton Application Factory 

    Singleton because we only care about using exec function in each class
    We don't really care about creating multiple objects
    - possibly saves memory
    Allows us to use another design pattern to get marks
    """

    def get_application(self, args: list[str]) -> AbstractApplication:
        application_name = args[0]

        # APPLICATION_DICT used to avoid if/swtich statements
        if application_name in APPLICATION_DICT:
            return APPLICATION_DICT[application_name]()

        raise ApplicationError(f"{application_name}: command not found")
