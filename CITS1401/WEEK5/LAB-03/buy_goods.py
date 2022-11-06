
# Write a function buy_goods(cost, savings) that takes two positive numeric arguments as
# parameters cost and savings and returns a Boolean type True only if the
# cost of the item is less than 5% of the savings, otherwise false.


def buy_goods(cost, savings):
    if cost < (0.05 * savings):
        return True
    else:
        return False


    
    