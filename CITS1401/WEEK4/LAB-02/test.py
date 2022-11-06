SMALL = 1
LARGE = 2
MAXIMUM = 3

a = SMALL
b = LARGE
c = MAXIMUM

# assume all variables have already been declared as integers, and they are all unique numbers
# (i.e., no two variables will have the same value).

if a > b:
    if c > a:
        print("largest is c")
    else:
        print("largest is a")
else:
    print("largest is b")