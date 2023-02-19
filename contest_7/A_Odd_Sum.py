size = int(input())
numbers = list(map(int, input().split()))

max_num = 0
max_idx = 0
for idx in range(size):
    num = numbers[idx]
    max_num = max(max_num, num)
    # if max_num is updated
    if max_num == num:
        max_idx = idx
        
min_num = float('inf')
min_idx = 0
for idx in range(size, len(numbers)):
    num = numbers[idx]
    min_num = min(min_num, num)
    # if max_num is updated
    if min_num == num:
        min_idx = idx
        
if max_num != min_num:
    numbers[max_idx], numbers[min_idx] = numbers[min_idx], numbers[max_idx]
    print(*numbers)
else:
    print(str(-1))