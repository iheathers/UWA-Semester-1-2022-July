def my_enumerate(items):
    
    indexed_items = []
    
    for i in range(len(items)):
        indexed_items.append((i, items[i]))
        
    return indexed_items

ans = my_enumerate([10, 20, 30])
print(ans)