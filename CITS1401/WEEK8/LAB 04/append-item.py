def append_item(data, item):
    data.append(item)
    
    return data

count = append_item([1, 2, 3, 4, 5], 1)
print(count)


count = append_item([1, 2, 1, 2, 1, 2], 2)
print(count)