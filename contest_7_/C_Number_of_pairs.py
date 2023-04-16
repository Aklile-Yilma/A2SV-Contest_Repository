num_boys = int(input())
boys = list(map(int, input().split()))
num_girls = int(input())
girls = list(map(int, input().split()))

pairs = 0

boys.sort()
girls.sort()

ptr1 = ptr2 = 0

while ptr1 < num_boys and ptr2 < num_girls:
    diff = abs(boys[ptr1] - girls[ptr2]) 
    
    if diff == 0 or diff == 1:
        pairs += 1
        ptr1 += 1
        ptr2 += 1
    elif boys[ptr1] < girls[ptr2]:
        ptr1 += 1
    else:
        ptr2 += 1
        
print(pairs)
       
        