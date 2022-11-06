def square(num):
    """Returns a given number squared"""
    return num * num

print(square(3))
print(type(square(3)))
      
print(square(3.0))
print(type(square(3.0)))

def to_celsius(temp_f):
    """Converts a given fahrenheit temperature to celsius"""
    return (temp_f - 32) * 5 / 9

print(to_celsius(212))

print(to_celsius(32))


def celsius(temp_f):
    """Converts a given fahrenheit temperature to celsius"""
    freezing = 32
    factor = 5 / 9
    ans = (temp_f - freezing) * factor
    return ans

print(celsius(32))


def distance_travelled(duration, speed):
    """Returns the distance travelled given duration and the speed"""
    return speed * duration