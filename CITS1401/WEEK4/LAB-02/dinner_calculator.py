def dinner_calculator(meal_cost, drinks_cost):
    """ Calculate the cost of dinner during happy hour.
        Takes into consideration:
         - Pre-GST meal and drink costs
         - Happy Hour discounts
         - GST
    """
    if (drinks_cost > 0):
        drinks_cost = drinks_cost - 0.3 * drinks_cost
        
    cost_before_GST = meal_cost + drinks_cost    
    cost_after_GST = cost_before_GST + 0.15 * cost_before_GST
    
    return round(cost_after_GST, 2)
    
    