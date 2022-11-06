def insert_item_end(data, item):
    data.insert(len(data), item)
    
    return data


count = insert_item_end([1, 2, 3, 4, 5], 1)
print(count)


count = insert_item_end([1, 2, 1, 2, 1, 2], 2)
print(count)
    