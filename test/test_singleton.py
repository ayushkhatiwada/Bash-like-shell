import unittest

from singleton import Singleton


class TestSingleton(unittest.TestCase):
    def test_singleton(self):
        class TestClass(Singleton):
            def init(self, *args, **kwds):
                self.args = args
                self.kwds = kwds

        obj1 = TestClass("foo", bar="baz")
        obj2 = TestClass("bar", baz="foo")

        self.assertEqual(obj1, obj2)
        self.assertEqual(obj1.args, ("foo",))
        self.assertEqual(obj1.kwds, {"bar": "baz"})
        self.assertEqual(obj2.args, ("foo",))
        self.assertEqual(obj2.kwds, {"bar": "baz"})
