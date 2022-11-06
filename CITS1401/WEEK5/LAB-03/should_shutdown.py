# Write a function should_shutdown(battery_level, time_on)
# which returns True when time_on is less than 60 and battery_level is less than 4.7.
# If time_on is greater than or equal to 60, return True if battery_level is less than 4.8.
# In all other situations the function returns False.
# 
# Read through the test cases and expected output to make sure you understand the description.

def should_shutdown(battery_level, time_on):
    if (time_on < 60 and battery_level < 4.7):
        return True
    elif (time_on >= 60 and battery_level < 4.8):
        return True
    else:
        return False

