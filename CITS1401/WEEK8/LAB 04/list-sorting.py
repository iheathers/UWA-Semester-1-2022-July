lst1 = ['a', 'ba', 'd', 'c', 'a']
lst2 = [5, 2, 3, 4, 2]



def list_sorting(lst1,lst2): 
    if len(lst1) == len(lst2):        
        employees_and_age = []
        
        for i in range(len(lst1)):
            employees_and_age.append((lst1[i], lst2[i]))
            
        sorted_by_name = sorted(employees_and_age)    
        sorted_by_age = sorted(sorted_by_name, key=lambda x: x[1], reverse=True)
        
        names = []
        ages = []            
        
        for name, age in sorted_by_age:            
            names.append(name)
            ages.append(age)
        
        return names, ages
        
        
print(list_sorting(lst1, lst2))
    