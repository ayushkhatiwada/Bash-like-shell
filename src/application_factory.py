from typing import List

from singleton import Singleton
from applications.application import Application, ApplicationError
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
    Singleton Application Factory

    Singleton because we only care about using exec function in each class
    Possibly saves memory
    """

    def get_application(self, args: List[str]) -> Application:
        application_name = args[0]

        # APPLICATIONS dict used to avoid if/swtich statements
        if application_name in APPLICATIONS:
            return APPLICATIONS[application_name]()
        raise ApplicationError(f"{application_name}: command not found")
