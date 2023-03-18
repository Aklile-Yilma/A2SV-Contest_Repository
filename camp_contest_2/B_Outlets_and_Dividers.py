num_test_cases = int(input())

for _ in range(num_test_cases):
    num_students, num_outlets = list(map(int, input().split()))
    divider_outlets = list(map(int, input().split()))
    NotFound = True
    
    answer = 0
    if  num_students <= 2:
        NotFound = False
    
    if NotFound:
        #sort outlets in reverse to find min value
        divider_outlets.sort(reverse=True)
        #compute prefix sum
        prefix = 2
        for idx in range(num_outlets):
            prefix = prefix + divider_outlets[idx] - 1
            if num_students <= prefix:
                answer = idx + 1
                NotFound = False
                break
            
        if NotFound:
            answer = -1
        
    print(answer)
        
                
    
        

        
         
    
    

