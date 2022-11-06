# A list of people's ages and names are provided in two separate lists age_list and name_list,
# and they are indexed for each person (e.g. person 1's information is at age_list[1] and name_list[1]). 
# 
# Write a function locate_person(age_list, name_list, age, name) which
# returns the index of the first person that has age equal to age and the name equal to name.
# You can assume there is always a person that matches the description, and names in the name_list are unique.

# def locate_person(age_list, name_list, age, name):
#     age_index = age_list.index(age)
#     name_index = name_list.index(name)
#     
#     if age_index == name_index:
#         return age_index
#     
#     
#     
#     
# print(locate_person([15, 7, 3, 9, 11, 6, 8], ["David", "Tom", "Mary", "Sam", "Harry", "Abby", "Nigel"], 3, "Mary"))
# print(locate_person([15, 7, 3, 9, 11, 6, 8], ["David", "Tom", "Mary", "Sam", "Harry", "Abby", "Nigel"], 11, "Harry"))


def locate_person(age_list, name_list, age, name):
    if (len(age_list) != len(name_list)):
        return
    
    for i in range(len(age_list)):
        if age_list[i] == age and name_list[i] == name:
            return i