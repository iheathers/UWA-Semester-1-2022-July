# Assume binary represents an unsigned binary number of arbitrary length.
# Write a function binarytodecimal(binary) to calculate the decimal equivalent of binary.
# Pass the binary number as a parameter of type str (string) to the function.
# 
# For example, if binary = '00000100', its decimal equivalent is 4. 
# 
# Try your algorithm out by entering each step into Python and make sure it works.


def binarytodecimal(binary):
    decimal_equivalent = 0    
    reveresed_binary = binary[::-1]
    
    for i in range(len(binary)):
        decimal_equivalent += int(reveresed_binary[i]) * 2**i

    return decimal_equivalent


    
    
