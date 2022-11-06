# Write a function bmi_risk(bmi, age) that takes two positive numeric arguments as parameters bmi and age and
# returns a string Low, Medium, or High according to the following table:

#                      Under 45            # 45 or over
# 
# BMI less than 22     Low                 Medium
# BMI 22 or more       Medium              High





def bmi_risk(bmi, age):
    if (age < 45):
        if (bmi < 22):
            return "Low"
        else:
            return "Medium"
    else:
        if (bmi < 22):
            return "Medium"
        else:
            return "High"
        
        
    
    