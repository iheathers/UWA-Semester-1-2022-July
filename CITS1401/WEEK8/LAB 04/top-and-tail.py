'''
Write a function top_and_tail(string) that takes a string as a parameter and returns the string with
its first and last characters removed. You may assume the string has at least one character in it.

Hint: this does not require a for loop

+─────────────────────────────────────────────+────────────────────+
| Test                                        | Result             |
+─────────────────────────────────────────────+────────────────────+
| print(top_and_tail('stubby'))               | tubb               |
| print(top_and_tail('another test string'))  | nother test strin  |
+─────────────────────────────────────────────+────────────────────+

'''


def top_and_tail(string):
    return string.strip(f"{string[0]}{string[-1]}")
    
    
    
    
print(top_and_tail('stubby'))     
print(top_and_tail('another test string'))   