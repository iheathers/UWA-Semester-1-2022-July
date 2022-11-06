def long_enough(strings, min_length):
    min_length_strings = []
    
    for word in strings:
        if len(word) >= min_length:
            min_length_strings.append(word)
            
    return min_length_strings

strings = ['a', 'bc', 'def', 'ghij', 'klmno']
print(long_enough(strings, 2))