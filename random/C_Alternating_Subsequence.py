num_test_cases = int(input())

for _ in range(num_test_cases):
    size = int(input())
    numbers = list(map(int, input().split()))
    
    max_sum = 0
    
    curr_max = numbers[0]
    idx = 0

    for idx in range(1, size):
        if numbers[idx] * numbers[idx-1] < 0:
            max_sum += curr_max
            curr_max = numbers[idx]
        else: 
            curr_max = max(curr_max, numbers[idx])
    max_sum += curr_max
    print(max_sum)        
            
            
        
        
    
    # while idx < size:
    #     # isPositive = True if numbers[idx] >= 0 else False
        
    #     while numbers[idx] >= 0:
    #         max_positive = max(max_positive, numbers[idx])
    #         idx += 1
    #         continue
    #     max_sum += max_positive
    #     max_positive = 0
        
    #     while numbers[idx] < 0:
    #         min_negative = max(min_negative, numbers[idx])
    #         idx += 1
    #         continue
        
    #     if min_negative != float('-inf'):
    #         max_sum += min_negative
    #         min_negative = float('-inf')
    
    


