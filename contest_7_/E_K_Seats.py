row_size, col_size, k = list(map(int, input().split()))
classroom = []

for _ in range(row_size):
    classroom.append(list(input()))
    
count = 0
#iterate by row
for row in range(row_size):
    empty_slots = 0
    for col in range(col_size):
        
        if classroom[row][col] == ".":
            empty_slots += 1
        else:
            empty_slots = 0
            
        if empty_slots >= k:
            count += 1

#iterate by col
for col in range(col_size):
    empty_slots = 0
    for row in range(row_size):
        
        if classroom[row][col] == ".": 
            empty_slots += 1
        else:
            empty_slots = 0
            
        if empty_slots >= k:
            count += 1
            
if k == 1:
    count //= 2
    
print(count)