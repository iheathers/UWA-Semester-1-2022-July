def nextRound(k,scores):
    
    if (1 <= k <= 20):
        count = 0
        
        for score in scores:
            if (score > 0 and score >= scores[k-1]):
                count = count + 1            
            
        return count

print(nextRound(10,[10,9,8,7,6,6,6,5,4]))
print(nextRound(2,[0,0,0,0]))