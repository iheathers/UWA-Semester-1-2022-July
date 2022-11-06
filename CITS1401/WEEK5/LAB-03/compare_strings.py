# Write a function compare_strings(string1, string2) which returns the larger string based on the length
# of the string if their first letters are the same (e.g. "band" and "bread" as inputs, "bread"
# will be returned because the length is longer), if their lengths are the same, then the function returns "error".
# On the other hand, if their first letters are different, then their last letters are compared and the string with
# the character that will appear later in the dictionary is returned (e.g. with "sky" and "cloud" as inputs, "sky"
# will be returned because 'y' comes after 'd' in the dictionary). One exception to the second case is that, if
# the last letters of each string are the same, then the function is to return "error".


def compare_strings(string1, string2):
    if (string1[0] == string2[0]):
        if (len(string1) > len(string2)):
            return string1
        elif (len(string1) < len(string2)):
            return string2
        else:
            return "error"
    else:
        if (string1[-1] > string2[-1]):
            return string1
        elif (string1[-1] < string2[-1]):
              return string2
        else:
            return "error"
            
   
        
    
    