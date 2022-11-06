# Write a boolean function check_temperature(temperature, limit)
# that takes floats temperature and limit, where temperature is in degrees Celsius
# and limit is in Fahrenheit, and returns True if limit is greater than the temperature in the same metric,
# else returns False. You may find the equation below useful.
# 
# fahrenheit = celsius x 9 / 5 + 32

def check_temperature(temperature, limit):
    fahrenheit_temperature = temperature  * 9 / 5 + 32
    
    if (limit > fahrenheit_temperature):
        return True
    else:
        return False
