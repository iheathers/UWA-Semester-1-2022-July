def singleDigit(N):
    
    while (N > 9):
        N = N % 10 + N // 10
    
    return N

print(singleDigit(10))
print(singleDigit(198))
        
    
#     remainder = N % 10
#     N = N // 10
#     
#     
#     result = remainder + N