def list_swap(lst):
    for i in range(0, len(lst) -1, 2):        
       lst[i], lst[i+1] =  lst[i+1], lst[i]
    
    return lst


print(list_swap([1,2,3,4,5]))
print(list_swap([12,32,54,24,51,23.54]))
print(list_swap([-1,7,[3,4],"Joe",90,[33],"True"]))