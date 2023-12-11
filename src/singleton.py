"""
Singleton class from official python documentation:
https://www.python.org/download/releases/2.2/descrintro/#__new__

Subclass from Singleton to create a singleton class

To further initialize the subclass instance,
subclasses should override 'init' instead of
__init__ - the __init__ method is called each time
the constructor is called.
"""


class Singleton(object):
    def __new__(cls, *args, **kwds):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwds)
        return it

    def init(self, *args, **kwds):
        pass
