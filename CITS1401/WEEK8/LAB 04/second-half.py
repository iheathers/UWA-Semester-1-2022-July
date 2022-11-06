"""
Write a function second_half_string(string) that takes a string as a parameter and returns 
the second half of the string. You may assume the string has at least one character in it. 
If the string length is odd, then you may assume it returns (𝑛+1)2 many characters
(e.g., string = 'hello', returns 'llo') where n represents the number of characters in the original string.

+─────────────────────────────────────────+─────────+
| Test                                    | Result  |
+─────────────────────────────────────────+─────────+
| print(second_half_string('stubby'))     | bby     |
| print(second_half_string('spongebob'))  | gebob   |
+─────────────────────────────────────────+─────────+

"""


def second_half_string(string):
    index = len(string) // 2

    return string[index:]


print(second_half_string('stubby'))
print(second_half_string('spongebob'))
