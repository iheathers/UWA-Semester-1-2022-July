def sequence(n):    
    pattern = [n]
    
    while n != 1:    
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
            
        pattern.append(int(n))
    
    return pattern

print(sequence(12))
# [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]

print(sequence(13))
# [20, 10, 5, 16, 8, 4, 2, 1]