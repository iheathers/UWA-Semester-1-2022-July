'''
Write a function count_word(sentence, word) that takes 'sentence' (a string) and 'word'
(another string) as parameters and returns the number of times the 'word' appears in 'sentence'.
Note, 'word' in this case can be any string, it does not necessarily have to be limited to
a standalone English word that is normally surrounded by spaces.
You may assume the sentence has at least one character in it.

Hint: this does not require a loop
'''


def count_word(sentence, word):
    return sentence.count(word)
    
print(count_word('stubby', 'b'))
print(count_word('1213141516171819', '1'))