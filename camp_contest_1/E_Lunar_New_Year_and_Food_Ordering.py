num_foods, num_customers = list(map(int, input().split()))
dishes = list(map(int, input().split()))
costs = list(map(int, input().split()))


cost_index = [(costs[idx], idx) for idx in range(len(costs))] 
cost_index.sort()
cheapest_by_idx = [idx for cost, idx in cost_index]
left = 0

for idx in range(num_customers):
    dish, amount = list(map(int, input().split()))
    #1-index 
    dish = dish - 1
    customer_payment = 0
    available_amount = dishes[dish]
    dish_cost = costs[dish]
    
    if available_amount >= amount:
        dishes[dish] -= amount
        customer_payment = amount * dish_cost
        amount = 0
    else:
        if available_amount > 0:
            dishes[dish] = 0
            amount -= available_amount
            customer_payment = available_amount * dish_cost
        
        while left < num_foods and amount > 0:
            cheap_idx = cheapest_by_idx[left]
            # print("cheap idx",cheap_idx)
            cheap_available_amount = dishes[cheap_idx]
            cheap_dish_cost = costs[cheap_idx]
            
            if cheap_available_amount >= amount:
                dishes[cheap_idx] -= amount
                customer_payment += amount * cheap_dish_cost
                amount = 0
            elif cheap_available_amount > 0:
                dishes[cheap_idx] = 0
                amount -= cheap_available_amount
                customer_payment += cheap_available_amount * cheap_dish_cost
            
            if dishes[cheap_idx] == 0: 
                left += 1 
                
            #if there are not enough dishes
            if left >= num_foods:  
                if amount > 0:
                    customer_payment = 0
            

    print(customer_payment)                

            
        
        
    
    
    
    
     
    
    
    
    
    
    
    
    