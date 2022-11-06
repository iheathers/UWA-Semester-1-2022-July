# The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...# 
# The next number is found by adding up the two numbers before it.

# Write a program to generate Fibonacci Sequence and print the nth number where n is taken as input from the use.

# For instance, if user inputs 9 (n=9) then 21 should be printed.
# Input: 9 --> Output: 21


n = int(input())
#Don't change the above line of code. Write your program below this line. Remember to print the final result only.

fibonacci_1 = 0
fibonacci_2 = 1

fibonacci_nth = 0
sum_of_fibonacci = 0

if n <= 0:
    print("Enter positive number")

else:
    for i in range(n):
        fibonacci_nth = fibonacci_1
        
        sum_of_fibonacci = sum_of_fibonacci + fibonacci_nth
        
        fibonacci_n = fibonacci_1 + fibonacci_2
        fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_n
    print(sum_of_fibonacci)