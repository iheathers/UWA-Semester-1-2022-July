def repeat_last(data):
    new_list = data[:]
    new_list.append(new_list[-1])
    
    return new_list


item = repeat_last([1,2,3])
print(item)


item = repeat_last(['hi'])
print(item)