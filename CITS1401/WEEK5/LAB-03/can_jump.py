# We are in a long jump competition with various athletes.
# Some athletes are injured so their performance can be affected. These are the variables used:
# 
# speed is the running speed in m/s (float value greater than 0).
# power is the strength to jump (float value between 0 and 1). 
# name is the jumper's name (string).
# injured is whether the jumper is injured or not (boolean).
# If injured, the distance the jumper will jump is decreased by 20%.
# 
# For example, if Brian is running at 9m/s with a strength of 0.6 without any injuries, he can jump 0.6 * 9 = 5.4m.
# 
# For example, if Morrison is running at 9m/s with a strength of 0.6 but with an injury,
# he can jump 0.8 * 0.6 * 9 = 4.32m.
# 
# Write a function can_jump(speed, power, name, injured) which returns a string "[name] can jump [distance]m!",
# where "distance" is formatted to 2 decimal places. However, if the jumper jumps less than a metre,
# then the function is to return the string "[name] made a false attempt!"
# 
# Be careful with printing text.

#speed > 0
# 0< power<1
# injured - boolean
# name - string


def can_jump(speed, power, name, injured):
    if not injured:     
        distance = speed * power    
    else:
        distance = 0.8 * speed * power
    
    if (distance < 1):
        return f'{name} made a false attempt!'
    else:
        return f'{name} can jump {distance:.2f}m!' 
              
    

        
        
    
    