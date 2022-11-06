def num_words(string):
    word_list = string.split(' ')
    
    return len(word_list)

word_count = num_words("Welcome to lists!")
print(word_count)

word_count = num_words("thi01234&*9 &^%x 1")
print(word_count)