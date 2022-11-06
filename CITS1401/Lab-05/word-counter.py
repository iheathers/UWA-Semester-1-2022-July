def word_counter(input_str):    
    lower_input_str = input_str.lower()       
    words = lower_input_str.split()
    
    word_count_dict = {}    
    
    for word in words:
        if word not in word_count_dict:
            word_count_dict[word] = 1            
        else:
            word_count_dict[word] = word_count_dict[word] + 1            
    
    return word_count_dict
    
    
word_count_dict = word_counter("This is a sentence")
items = word_count_dict.items()
sorted_items = sorted(items)
print(sorted_items)

word_count_dict = word_counter("A WORD is a word it is")
items = word_count_dict.items()
sorted_items = sorted(items)
print(sorted_items)