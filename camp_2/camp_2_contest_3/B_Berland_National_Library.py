n = int(input())

seen = set()
initial_num = 0
data = []
for _ in range(n):
    sign, reg_id = input().split()
    if sign == '-' and ('+', reg_id) not in seen:
        initial_num += 1
    seen.add((sign, reg_id))
    data.append((sign, reg_id))

min_capacity = initial_num
curr = initial_num
seen = set()
for sign, reg_id in data:
    if sign == '+':
        curr += 1
        min_capacity = max(min_capacity, curr)
    else:
        curr -= 1
        min_capacity = max(min_capacity, curr)

print(min_capacity)

