# def record_check(age, gender, location):
#     """ Function to find a male person depending on their age, gender and location """
#     if age > 18:
#         if gender == "M":
#             if location == "Perth":
#                 print("Found him!")
#             elif location == "Sydney":
#                 print("Found him!")
#             else:
#                 print("Did not find him.")
#         else:
#             print("Did not find him.")
#     else:
#         print("Did not find him.")

def record_check(age, gender, location):
    if (age > 18 and gender =="M" and (location =="Perth" or location =="Sydney")):
        print("Found him!")
    else:
        print("Did not find him.")
        