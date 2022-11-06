def remove(data):
    data.remove(data[1])
    
    return data


last_item = remove([10, 20, 40, 80])
print(last_item)


last_item = remove([1, 2])
print(last_item)