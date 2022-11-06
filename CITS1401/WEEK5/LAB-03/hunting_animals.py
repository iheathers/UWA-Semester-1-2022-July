# A hunter takes n bullets to hunt. On a sunny day, his accuracy is high so it only takes 1 bullet to hunt a rabbit,
# and 2 bullets to hunt a deer. But on a rainy day, his accuracy drops and takes 2 bullets to hunt a rabbit
# and 3 bullets to hunt a deer. 
# 
# Write a function hunting_animals(weather, animal, n) which returns the number of animal he successfully
# caught on that day.
# 
# weather values are either "sunny" or "rainy".
# 
# animal values are either "rabbit" or "deer"
# 
# n value is a positive integer 0 < n < 100.

RABBIT = "rabbit"
DEER = "deer"

SUNNY = "sunny"
RAINY = "rainy"

SUNNY_RABBIT_BULLET = 1
SUNNY_DEER_BULLET = 2

RAINY_RABBIT_BULLET = 2
RAINY_DEER_BULLET = 3

def hunting_animals(weather, animal, n):
    if (n > 0 and n < 100):
        if (weather == SUNNY and animal == RABBIT):
            return int(n/SUNNY_RABBIT_BULLET)
        
        if (weather == SUNNY and animal == DEER):
            return int(n/SUNNY_DEER_BULLET)
        
        if (weather == RAINY and animal == RABBIT):
            return int(n/RAINY_RABBIT_BULLET)
        
        if (weather == RAINY and animal == DEER):
            return int(n/RAINY_DEER_BULLET)
        
    