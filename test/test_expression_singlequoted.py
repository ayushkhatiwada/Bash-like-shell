import unittest
import shell
from expressions import SingleQuoted

class TestSingleQuoted(unittest.TestCase):
    def test_singlequoted_init(self):
        children = ["child1", "child2"]
        sq = SingleQuoted(*children)
        self.assertEqual(sq.children, children)

    def test_singlequoted_str(self):
        children = ["child1", "child2"]
        sq = SingleQuoted(*children)
        self.assertEqual(str(sq), "SingleQuoted(['child1', 'child2'])")

    def test_singlequoted_eq(self):
        children1 = ["child1", "child2"]
        children2 = ["child2", "child1"]
        sq1 = SingleQuoted(*children1)
        sq2 = SingleQuoted(*children1)
        sq3 = SingleQuoted(*children2)
        self.assertEqual(sq1, sq2)
        self.assertNotEqual(sq1, sq3)

    def test_singlequoted_eval(self):
        children = ["child1", "child2"]
        sq = SingleQuoted(*children)
        result = sq.eval()
        self.assertEqual(result, "child1child2")
