def score(mid, times):
    size =  len(times) - 1
    
    score = 0
    for idx in range(size):
        
        if (times[idx + 1] - times[idx]) < mid:
            score += (times[idx + 1] - times[idx])
        else:
            score += mid
            
    return score

num_test_cases = int(input())

for _ in range(num_test_cases):
    n, h = list(map(int, input().split()))
    times = list(map(int, input().split()))
    times.append(float('inf'))
    
    low = 1
    high = h
    
    while low <= high:
        mid = low + (high - low)//2
        curr_score = score(mid, times)
        
        if curr_score >= h:
            high = mid - 1
        else:
            low = mid + 1
    
    print(low)
            
    
    
    