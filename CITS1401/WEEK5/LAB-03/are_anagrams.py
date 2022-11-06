# Two words are anagrams if they contains exactly the same letters but in a different order.
# Write a function are_anagrams(word1, word2) which returns True if the two parameters are anagrams.
# 
# Big hints:
# 
# You can convert a word into a list of the letters in that word.
# Lists of strings can be sorted into alphabetical order using the list.sort() method.
# The equality operator '==' works on lists.
# Two identical words are not anagrams.
# Hint: this can be done without a loop.

def are_anagrams(word1, word2):
    if (word1 == word2):
        return False
    
    else:
        word1_characters = list(word1)
        word2_characters = list(word2)
        
        word1_characters.sort()
        word2_characters.sort()   
        
        if (word1_characters == word2_characters):
            return True
        else:
            return False
        

    
    
    