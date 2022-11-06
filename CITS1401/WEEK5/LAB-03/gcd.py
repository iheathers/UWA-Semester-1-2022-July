#  Write a function gcd(num1,num2) that takes two integers and return GCD of the two input integers.
# You can assume that inputs will always be positive integers.

def gcd(num1, num2):    
    gcd = 1    
    smallest_number = num1 if num1 < num2 else num2
    
    for divisor in range(1, smallest_number + 1):  
        if (num1 % divisor == 0) and (num2 % divisor == 0):
            gcd = divisor
            
    return gcd

