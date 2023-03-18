from collections import Counter
recipe = Counter(input())
# bread, curr_sausage, curr_cheese = recipe['B'], recipe["S"], recipe['C']
num_bread, num_sausage, num_cheese = list(map(int, input().split()))
price_bread, price_sausage, price_cheese = list(map(int, input().split()))
rubles = int(input())

count = 0
# without
while (num_bread - recipe['B']) >= 0 and (num_sausage - recipe['S']) >= 0 and (num_cheese - recipe["C"] ) >= 0:
    count += 1
    num_bread -= recipe['B']
    num_sausage -= recipe['S']
    num_cheese -= recipe['C']
    
#buy from remaining

while rubles:
    bread_amount = recipe['B'] - num_bread if num_bread > 0 else recipe['B']
    cheese_amount = recipe['C'] - num_cheese if num_cheese > 0 else recipe['C']
    sausage_amount = recipe['S'] - num_sausage if num_sausage > 0 else recipe['S']
    
    total = (price_bread * bread_amount) + (price_cheese * cheese_amount) + (price_sausage * num_cheese)
    if total <= rubles:
        count += 1
        rubles -= total
    else:
        break
    
print(count)
    


