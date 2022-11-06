def get_name(name_dict, id_num):
    
    if (id_num not in name_dict):
        return None
    
    return name_dict[id_num]
    
    
    


test_dictionary = {11:'Fred', 2001:'Agnes'}
ans = get_name(test_dictionary, 2001)
print(ans)


test_dictionary = {11:'Fred', 2001:'Agnes'}
ans = get_name(test_dictionary, 10)
print(ans)