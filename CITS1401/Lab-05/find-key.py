def find_key(input_dict, value):
    input_dict_keys = input_dict.keys()
    
    for key in input_dict_keys:
        if input_dict[key] == value:
            return key
    
    return None
    

test_dictionary = {100:'a', 20:'b', 3:'c', 400:'d'}
print(find_key(test_dictionary, 'b'))


test_dictionary = {100:'a', 20:'b', 3:'c', 400:'d'}
print(find_key(test_dictionary, 'e'))