def run_length_encode(nums):
    result = []
    
    if len(nums) > 0:
        current = nums[0]    
        count = 0
        
        for num in nums:    
            if num == current:
                count += 1
            else:            
                result.append((current, count))            
                current = num
                
                count = 1
                
        
        result.append((current, count))
        
    return result  
    
        
    
                
                

print(run_length_encode([]))


data = [5, 5, 5, 10, 10]
print(run_length_encode(data))


data = [10, 20, 30, 30, 30, 30]
print(run_length_encode(data))