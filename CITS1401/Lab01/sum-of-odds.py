# Question: Write a program that can add first n positive odd numbers starting from 1
# the number n is entered by the user.

# Test conditions: The program should only work for positive input data and give zero output for negative data

# Author: Pritam Suwal Shrestha

n = int(input())

counter = 0
number = 1
sum_of_odds = 0

if n < 0:
    print(0)
else:
    while counter < n:
        if number % 2 != 0:
            counter += 1
            sum_of_odds += number
        number = number + 1
    print(sum_of_odds)