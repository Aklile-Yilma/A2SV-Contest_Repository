def check(sticks):
    left = 0
    right = len(sticks) -1
    
    while left <= right:
        if left == 0:
            left += 1
            right -= 1
            continue
        else:
            prev_area = sticks[left-1] * sticks[right+ 1]
            new_area = sticks[left] * sticks[right]
                
            if prev_area != new_area:
                return False
    
        left += 1
        right -= 1
        
    return True

num_queries = int(input())

for _ in range(num_queries):
    num_rec = int(input())
    sticks = list(map(int, input().split()))
    sticks.sort()
    pair_sticks = []
    isPossible = True
    for idx in range(0,len(sticks), 2):
        if sticks[idx] != sticks[idx + 1]:
            isPossible = False
            break
        pair_sticks.append(sticks[idx])
        
    if isPossible and len(set(pair_sticks)) == 1:
        print("YES")
    elif isPossible and check(pair_sticks):
        print("YES")
    else:
        print("NO")

        
    
    
    
    
    
    
    