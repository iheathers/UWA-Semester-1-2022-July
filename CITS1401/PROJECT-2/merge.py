def merge(list1, list2):
    count1 = 0
    count2 = 0

    sorted_list = []

    if len(list1) < len(list2):
        shorter_list = list1
        longer_list = list2
    else:
        shorter_list = list2
        longer_list = list1

    while count1 < len(shorter_list) and count2 < len(shorter_list):
        if shorter_list[count1] < longer_list[count2]:
            sorted_list.append(shorter_list[count1])
            count1 += 1
        else:
            sorted_list.append(longer_list[count2])
            count2 += 1

        print(sorted_list)

    return sorted_list + shorter_list[count1:] + longer_list[count2:]


print(merge([0, 2, 4, 6, 8, 9], [1, 3, 5]
            ))
