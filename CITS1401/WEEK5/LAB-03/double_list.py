# Write a function double_list(items) that takes a list items and returns a list
# that has been duplicated (see the examples below)
# if the number of items in the list is even, otherwise it returns a list
# that is the same as items but with only the last item repeated.

def double_list(items):
    if len(items) % 2 == 0:
        doubled_items = items + items
        return doubled_items
    else:
        items.append(items[-1])
        return items