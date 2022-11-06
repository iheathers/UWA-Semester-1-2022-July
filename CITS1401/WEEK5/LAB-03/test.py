# def month(n):
#     months_in_string = "JanFebMarAprMayJunJulAugSepOctNovDec"
#     n = (n-1)*3
#     print(months_in_string[n:n+3])
#     
# # month(4)
# 
# def months_in_list(n):
#     months = ["January", "February", "mar", "april", "may", "june", "jul", "aug", "sep", "oct", "nov", "dec"]
#     
#     print(months[n])
#     
# months_in_list(20)


intlist = []

for i in range(6):
    if i%2 == 0:
        intlist.append(i)
    else:
        intlist[-1] +=1
        
print(intlist)