from abc import ABC, abstractmethod


# Cannot instantiate abstract bird class
class Bird(ABC):

    # Any classes which inherit Bird must implement the abstract talk method or error is thrown
    @abstractmethod
    def talk(self) -> None:
        pass


class Parrot(Bird):

    def talk(self) -> str:
        return "I am a parrot"


class Penguin(Bird):

    def talk(self) -> str:
        return "I am a penguin"

"""
Dynamic Dispatch
----------------
function lets_hear does not know which talk() method it is calling
talk() method behaves differently depending on the type of Bird b
This is better than having several if, else statements
Use this technique in this cwk
"""
def lets_hear(b: Bird) -> None:
    print(b.talk())

lets_hear(Parrot())
lets_hear(Penguin())
