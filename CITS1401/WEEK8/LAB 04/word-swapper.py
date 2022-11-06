'''
Write a function word_swapper(sentence, word) that takes 'sentence' and 'word' as parameters,
replaces every 'word' in the 'sentence' with 'ABC'. You may assume the string has at least one character in it.

+───────────────────────────────────────────────────────────────────+─────────────────────────────────────+
| Test                                                              | Result                              |
+───────────────────────────────────────────────────────────────────+─────────────────────────────────────+
| print(word_swapper('This is a sentence.', 'is'))                  | ThABC ABC a sentence.               |
| print(word_swapper('coding is cool but coding is hard!', 'cod'))  | ABCing is cool but ABCing is hard!  |
+───────────────────────────────────────────────────────────────────+─────────────────────────────────────+

'''


def word_swapper(sentence, word):
    return sentence.replace(word, 'ABC')
    
    
print(word_swapper('This is a sentence.', 'is'))
print(word_swapper('coding is cool but coding is hard!', 'cod')) 