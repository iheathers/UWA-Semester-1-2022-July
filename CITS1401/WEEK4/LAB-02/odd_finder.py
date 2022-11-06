def odd_finder(a,b,c,d,e,f,g,h,i,j):
    count = 0    
    numbers = [a, b, c, d, e, f, g, h, i, j]
    
    for number in numbers:
        if number > 0 and (number %  2) != 0:
            count = count + 1
            
    return(count)