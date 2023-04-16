num_test_cases = int(input())

for _ in range(num_test_cases):
    numbers = list(input())
    
    left= 0
    min_size = float('inf')    
    last_seen = {
        1: -1,
        2: -1,
        3: -1
    }
        
    for right in range(len(numbers)):
        last_seen[int(numbers[right])] = right
        
        if last_seen[1] != -1 and last_seen[2] != -1 and last_seen[3] != -1:
            left = min([last_seen[1], last_seen[2], last_seen[3]])
            min_size = min(min_size, right - left + 1)
    
    if min_size == float('inf'):
        print('0') 
    else:
        print(min_size)
            
            
        
            
        
            
        
    
