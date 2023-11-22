from abc import ABC, abstractmethod


class AbstractApplication(ABC):
    """
    Abstract Application class

    contains abstract exec function
    each command class (pwd, ls, cat etc.) will inherit Application class and the abstract exec function 
    each child class will overide the abstract exec function

    Dynamic dispatch will then be used
    """


    @abstractmethod
    def exec(self):
        pass


class ApplicationError(Exception):
    """Raised when an error occurs when calling an application"""
