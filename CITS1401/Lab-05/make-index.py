def make_index(words_on_page):    
    indexed_words = {}    
    pages = words_on_page.keys()
    
    for page in pages:
        for word in words_on_page[page]:
            
            valid_page = indexed_words.get(word)
            
            if not valid_page: 
                indexed_words[word] = [page]
            else:
                indexed_words[word].append(page)
    return indexed_words
        
    
    


input_dict = {
   1: ['hi','there', 'go'], 
   2: ['there', 'we', 'go'],
   3: ['fred', 'was', 'there']}
output_dict = make_index(input_dict)
for word in sorted(output_dict.keys()):
    print(word + ': ' + str(output_dict[word]))