def make_dictionary(filename):
    
    word_occurrences = {}
    
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            if not line.isspace():
                striped_line = line.strip()
                
                word_occurrences[striped_line] = word_occurrences.get(striped_line, 0) + 1
        
    return word_occurrences
                
                
        

# Testing with the example data in the question
dictionary = make_dictionary('lab8_object_files/data.txt')
for key in sorted(dictionary.keys()):
    print(key + ': ' + str(dictionary[key]))