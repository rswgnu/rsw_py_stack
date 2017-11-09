# rsw_py_stack
A featureful, polymorphic Python3 stack datatype (for educational purposes) offering:

* creation with any number of items: `s1 = Stack(0, 1, 2); s2 = Stack()`

* access to top item: `s1.top()` returns `2`; `s2.top()` returns `None`

* emptiness and boolean truthiness testing:<br>
          `s1.is_empty()` returns `False`; `s2.is_empty()` returns `True`<br>
		  `s1 and not s2` returns `True`

* pushing single items: `s2.push(2)` returns `Stack[2]`

* concatenation with '+' adds items of s2, from bottom to top, to s1: `s1 + s2` returns `s1 = Stack(0, 1, 2, '3')`

* duplication and extending with '*': `s1 * 2` returns `s1 = Stack[0, 1, 2, '3', 0, 1, 2, '3']`

* iteration: `for item in s1`  (iterates from top to bottom of Stack)

* containment for finding if an item is in the list: `if 2 in s1: print("found it")`

* extending by any number of items:<br>
          `s2.extend(3, 4)`  returns `Stack[2, 3, 4]`<br>
          `s3.extend(4, 5)`  returns `Stack['3', 4, 5]`

* counting item occurrences: `s2.count(3)` returns `1`

* conversion to a standard Python list of items:<br>
         from bottom to top: `s2.items()` returns `[2, 3, 4]`<br>
         from top to bottom: `s2.list()`  returns `[4, 3, 2]`

* a full set of self-tests: `Stack.test()`.
