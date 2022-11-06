def composite2(N):
    
    primes = []
    num = 1

    while len(primes) < N:        
        counter = 0
        
        for i in range(1, num+1):            
            if num % i == 0:
                counter = counter + 1
        
        if (counter > 2 and num % 2 != 0):
            primes.append(num)            
        
        num = num + 1        
    
    return primes[-1]
                
        

print(composite2(3))
print(composite2(5))