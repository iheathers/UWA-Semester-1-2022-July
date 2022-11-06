# A bit shift is a procedure that takes a binary string and moves the digits either left or right,
# wrapping digits around as required; e.g. a left shift of 1 applied to 10011 gives 00111,
# and a left-shift of 2 gives 01110.
# 
# Write a function bitshift(s,k,b) that takes a string s, an integer k,
# and a Boolean b, and returns s shifted by k, left if b is True, and right otherwise.
# 
# What will be the output of bitshift("110011",2,True)

# def bitshift(s, k, b):
#     string = s    
#     number_of_shifts = k
#     left_shift = b
#     
#     if (left_shift):
#         string_list = list(string)
#         
#         for i in range(number_of_shifts):
#             selected_character = string_list.pop(0)
#             
#             string_list.append(selected_character)
#         
#         return string_list
#             
# print(bitshift("10011",1,True))
# print(bitshift("110011",2,True))


def bitshift(s, k, b):
    old_string = s    
    number_of_shifts = k
    left_shift = b
    
    shifted_string = old_string
    
    for i in range(number_of_shifts):        
        if (left_shift):
            first_character = old_string[0]
            sliced_string = old_string[1:]            
            shifted_string = sliced_string + first_character            
            old_string = shifted_string            
        else:
            last_character = old_string[-1]
            sliced_string = old_string[:-1]
            shifted_string = last_character + sliced_string
            old_string = shifted_string            
    
    return shifted_string
        
        
    
print(bitshift("1",2,False))
print(bitshift("110011",2,False))     
            
    