"""
Write a function first_nth_string(string, n) that takes a string and an integer n as parameters and returns the
sliced string of the first n characters. You may assume that string contains at least n + 1 characters.

+────────────────────────────────────────────────────────────────+─────────+
| Test                                                           | Result  |
+────────────────────────────────────────────────────────────────+─────────+
| item = first_nth_string("this is some string", 4)              | this    |
| print(item)
+----------------------------------------------------------------+---------+
| item = first_nth_string("this is some string", 7)
| print(item)                                                      | this is |
+────────────────────────────────────────────────────────────────+─────────+

"""


def first_nth_string(string, n):
    return string[:n]


item = first_nth_string("this is some string", 4)
print(item)

item = first_nth_string("this is some string", 7)
print(item)
