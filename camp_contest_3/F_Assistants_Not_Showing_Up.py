num_days, num_assistants = list(map(int, input().split()))
available_days = []

for _ in range(num_assistants):
   start_end = list(map(int, input().split()))
   available_days.append(start_end)
      
available_days.sort()

start = float('inf')
end = -1
idx = 0

for a, b in available_days:
    start = min(start, a)
    if a <= end + 1 or idx == 0:
        end = max(end, b)
    idx += 1

if start != 0 or end != num_days - 1:
    print("YES")    
else:
    print('NO')
    
    
    
    
    
    
