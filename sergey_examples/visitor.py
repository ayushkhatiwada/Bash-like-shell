"""
Visitor

Problem: Separate algorithms from the objects on which they operate

Usage:
- When you need to perform an operation on all elements of a tree of objects
- Clean up the business logic of auxiliary behaviours
- When a behaviour makes sense only in some classes of a class hierarchy,
but not in others
"""

class Add:
    def eval(self):
        self.left + self.right