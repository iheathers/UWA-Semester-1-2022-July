# The inputs are:

# price: Fuel price in Litres
# distance: Distance to travel in kilometers
# economy: Fuel economy of the vehicle as L/100km

# The function returns the cost to travel in the vehicle (don’t include the dollar-sign, just return the real number).
# You are required to pass the arguments to the function in the same order as described.
# 
# What is the cost to travel for the following values. Do not include the units :
# 
# Price = $1.3 ; Distance = 10 Km ; Economy = 5 L/100Km

def trip_cost(price,distance,economy):
    total_fuel_consumed = ((1/100) * economy) * distance
    
    total_fuel_cost = total_fuel_consumed * price
    
    return round(total_fuel_cost, 2)
    
    
