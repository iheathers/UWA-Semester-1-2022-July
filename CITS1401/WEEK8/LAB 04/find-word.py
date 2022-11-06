"""
Write a function find_word(sentence, word) that takes 'sentence' (a string) and 'word' (another string)
as parameters and returns the index of the first occurrence of 'word' in 'sentence'.
As with the previous question, 'word' in this case can be any string,
it is not necessarily a standalone English word that is normally surrounded by spaces.
You may assume that 'sentence' has at least one character in it, and that 'word' exists in 'sentence'.

Hint: check the functions of strings
"""


def find_word(sentence, word):
    return sentence.find(word)

