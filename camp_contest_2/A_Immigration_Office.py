size = int(input())
names = list(input().split())
num_queries = int(input())

for _ in range(num_queries):
    query = input()
    
    low = 0
    high = size-1
    
    while low <= high:
        mid = (low + high) // 2
        
        if query < names[mid]:
            high = mid - 1
        elif query > names[mid]:
            low = mid + 1
        else:
            low = mid
            break
        
    print(low)
        