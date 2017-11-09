#!/usr/bin/python3
#
# SUMMARY:      A featureful, polymorphic Python3 stack datatype (for educational purposes)
# USAGE:        'stack.py' to run self-tests; 'import stack; stack = Stack(*items)' to create a Stack
#
# AUTHOR:       Bob Weiner
#
# LICENSE:      MIT License
# COPYRIGHT:    Copyright (C) 2017  Bob Weiner
#
# LAST-MOD:      9-Nov-17 at 16:38:16 by Bob Weiner
#
# DESCRIPTION:  
"""
A featureful, polymorphic Python3 stack datatype (for educational purposes) offering:

        creation with any number of items: s1 = Stack(0, 1, 2); s2 = Stack(); s3 = Stack('3')

        access to top item: s1.top() returns 2; s2.top() returns None

        emptiness and boolean truthiness testing:
           s1.is_empty() returns False; s2.is_empty() returns True
           s1 and not s2 returns True

        pushing single items: s2.push(2) returns Stack[2]

        concatenation with '+' adds items of s2, from bottom to top, to s1: s1 + s2 returns s1 = Stack(0, 1, 2, '3')

        duplication and extending with '*': s1 * 2 returns s1 = Stack[0, 1, 2, '3', 0, 1, 2, '3']

        iteration: for item in s1  (iterates from top to bottom of Stack)

        containment for finding if an item is in the Stack: if 2 in s1: print("found it")

        extending by any number of items:
          s2.extend(3, 4)  returns Stack[2, 3, 4]
          s3.extend(4, 5)  returns Stack['3', 4, 5]

        counting item occurrences: s2.count(3) returns 1

        conversion to a standard Python list of items:
            from bottom to top: s2.items() returns [2, 3, 4]
            from top to bottom: s2.list()  returns [4, 3, 2]

        a full set of self-tests: Stack.test().
"""
# DESCRIP-END.

from numbers import Integral

class Stack(object):

    def __init__(self, *items):
        "Create a new Stack containing multiple 'items' pushed from first to last (last is top of stack)."
        self.index = 0
        self.elts = list(items)

    def count(self, item):
        return self.elts.count(item)

    def extend(self, *items):
        "Push 'items' from first to last onto the Stack."
        if type(items) in (tuple, list):
            self.elts.extend(items)
            return self
        else:
            raise TypeError("'items' argument must be a tuple or list")

    def is_empty(self):
        "Return True if Stack contains no items, else False."
        return len(self.elts) == 0

    def items(self):
        "Return a list of items on a Stack, from bottom to top."
        return self.elts

    def list(self):
        "Return a list of items on a Stack, from top to bottom."
        return list(reversed(self.elts))

    def pop(self):
        "Remove and return item from the top of the Stack or signal an IndexError if none."
        if len(self.elts) > 0:
           item = self.elts[-1]
           del self.elts[-1]
           return item
        else:
           raise IndexError("Stack is empty; can't pop")

    def push(self, item):
        "Add 'item' to the top of the Stack; use 'extend' to push multiple items."
        if len(self.elts) > 0:
            self.elts.append(item)
        else:
            self.elts = [item]
        return self

    def top(self):
        "Return the top item from the Stack or None when empty."
        return self.elts[-1] if len(self.elts) > 0 else None

    def __add__(self, stack):
        "Push 'stack' items from bottom to top onto self."
        self.elts.extend(stack)
        return self

    def __mul__(self, num):
        """
        Push existing Stack items onto itself 'num' - 1 times.  Return empty Stack if 'num' is 0.
        Raise TypeError if 'num' is non-integral or less than 0.
        """
        if isinstance(num, Integral) and num >= 0:
            if num == 0:
                return Stack()
            else:
                items = self.elts
                for i in range(num - 1):
                    self.extend(*items)
                return self
        else:
            raise TypeError("Multiplier must be a non-negative integer but is: %s" % num)

    def __bool__(self):
        return bool(self.elts)

    def __contains__(self, item):
        return item in self.elts

    def __eq__(self, stack):
        return type(self) is type(stack) and self.elts == stack.elts

    def __iter__(self):
        self.index = len(self)
        return self

    def __len__(self):
        "Return the number of Stack items."
        return len(self.elts)

    def __next__(self):
        if self.index <= 0 or self.is_empty():
            self.index = len(self)
            raise StopIteration
        else:
            self.index -= 1
            return self.elts[self.index]

    def __repr__(self):
        "Return the printable representation of a Stack." 
        return "Stack" + str(self.elts) if self.elts else "[]"

    def test():
        "Run Stack self-tests."
        # Make these Stacks global so can be used after test() runs.
        global s1, s2, s3, s4
        s1 = Stack()
        s2 = Stack(0, 1, 2, 3)
        s3 = Stack("elt", [1, 2], 3)
        s4 = Stack(0, 1, 2, 3)

        assert [x for x in s4] == [3, 2, 1, 0]

        assert not s1
        assert s1.is_empty()
        assert not s1.top()
        assert s2
        assert not s2.is_empty()
        assert 2 in s2
        assert 6 not in s2
        assert len(s2) == 4
        assert len(s3) == 3
        assert not s1 == s2
        assert s2 == s4
        assert s1.count(3) == 0
        assert s2.count(3) == 1
        assert s3.count([1, 2]) == 1

        assert not s1.top()
        assert s2.top() == 3
        assert s2.push(4) == Stack(0, 1, 2, 3, 4)
        assert s2.items() == [0, 1, 2, 3, 4]
        assert s2.list()  == [4, 3, 2, 1, 0]
        assert s2.top() == 4
        assert s2.pop() == 4
        assert s2.top() == 3
        assert s3.pop() == 3
        assert s3.pop() == [1, 2]
        assert s3.top() == "elt"
        assert s3.pop() == "elt"
        assert not s3
        try: s1.pop()
        except(IndexError): True
        try: s3.pop()
        except(IndexError): True

        s2 = Stack(0, 1, 2, 3)
        assert [x for x in s2] == [3, 2, 1, 0]
        assert s2*0 == Stack()
        assert s2*1 == s2
        assert s2*2 == Stack(0, 1, 2, 3, 0, 1, 2, 3)

        s1 = Stack(0, 1)
        s2 = Stack(2, 3)
        s1 + s2
        s1 == Stack(0, 1, 2, 3)
        s2 == Stack(2, 3)
        s1.extend(4, 5) == Stack(0, 1, 2, 3, 4, 5)

        return True

if __name__ == "__main__":
    Stack.test()
