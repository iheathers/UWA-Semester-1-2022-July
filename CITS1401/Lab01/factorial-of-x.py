x = int(input(""))

factorial = 1

if x < 0:
    print("The factorial of negative number does not exist.")
else:
    for i in range(1, x + 1):
        factorial *= i
    print(factorial)