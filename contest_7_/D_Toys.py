from collections import Counter
num_tags, amount = list(map(int, input().split()))
prices = list(map(int, input().split()))
toys = []

for _ in range(amount):
    toys.append(input())
    
counter = Counter(toys)
items_count = list(counter.values())

#sort
items_count.sort(reverse=True)
prices.sort()

#find min
min_cost = 0
price_idx = 0
for idx in range(len(items_count)):
    min_cost += items_count[idx] * prices[price_idx]
    price_idx += 1
    

#find max 
max_cost = 0
price_idx = len(prices) - 1
for idx in range(len(items_count)):
    max_cost += items_count[idx] * prices[price_idx]
    price_idx -= 1

print(min_cost, max_cost)