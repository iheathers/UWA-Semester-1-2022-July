x = int(input())

# sum of squares of all numbers between zero and a whole number x that the user enters
# (x can be positive or negative).

# MAKE x POSITIVE
x = abs(x)

sum_of_squares = 0
    
for i in range(x+1):
    sum_of_squares += i**2

# The program must then print the result of this calculation to the shell.
print(sum_of_squares)
              
# TEST CASES
# For instance, if the user enters 5, then the sum of the squares of numbers 0, 1, 2, 3, 4 and 5 is 55,
# so your program should print 55 to the shell.
# Similarly the sum of squares for all numbers up to -4 is 30.


