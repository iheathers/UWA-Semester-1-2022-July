# Write a function my_abs(value) that returns the string mentioning whether the value is positive, negative or zero.
# The three possible outputs are "positive", "negative" or "zero". Remember the outputs are case sensitive. 
# 
# You are required to use an if statement for this question.

def my_abs(value):
    if (value > 0):
        return "positive"
    elif (value < 0):
        return "negative"
    else:
        return "zero"
    
    