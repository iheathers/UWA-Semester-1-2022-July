def series(x):
    
    sum = 0   
    power = 1    
    next_term = 1
    
    while x <= next_term:
        
        sum = sum + next_term
        next_term = 1 / (2 ** power)        
        power = power + 1
        
    return round(sum, 4)
    
print(series(0.5))
# 1.5

print(series(0.25))
# 1.75

print(series(0.05))
# 1.9375

print(series(0.01))
# 1.9844

print(series(0.001))
# 1.998
