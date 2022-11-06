"""
Write a function half_string(string) that takes a string as a parameter and returns the first half of the string.
You may assume the string has at least one character in it. If the string length is odd,
then you may assume it returns (𝑛−1)2 characters where n represents how many characters are in the original string
(e.g., string = 'hello', returns 'he').

+──────────────────────────────────+─────────+
| Test                             | Result  |
+──────────────────────────────────+─────────+
| print(half_string('stubby'))     | stu     |
| print(half_string('spongebob'))  | spon    |
+──────────────────────────────────+─────────+

"""


def half_string(string):
    if len(string) % 2 == 0:
        return string[:len(string) // 2]
    else:
        return string[:(len(string) - 1) // 2]


print(half_string('stubby'))
print(half_string('spongebob'))
