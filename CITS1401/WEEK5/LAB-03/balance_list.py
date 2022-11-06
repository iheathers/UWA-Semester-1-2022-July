# Write a function balance_list(items) that takes a list items
# which contains integers and returns the provided list if the number of items in the list is even,
# otherwise it returns the list but with its last item repeated
# (in order to make the number of items in the list even).

def balance_list(items):
    if len(items) % 2 == 0:
        return items
    else:
        items.append(items[-1])
        return items

