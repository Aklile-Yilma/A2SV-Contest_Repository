"approach was good and similar to the optimal one but it doesn't work for all cases"

num_test_cases = int(input())

for _ in range(num_test_cases):    
    num_integers, target_value = list(map(int, input().split()))
    integers = list(map(int, input().split()))
    
    integers.sort()

    found = False
    i , j = 0, 1
    while not found and j < num_integers:
        difference = integers[j] - integers[i]
        
        if difference == target_value:
            found = True
        elif difference > target_value:
            i += 1
        else:
            j += 1
    
    if found:
        print("YES")
    else:
        print("NO")
        
"""
previous appraoch
"""     
# num_test_cases = int(input())

# for _ in range(num_test_cases):    
#     num_integers, target_value = list(map(int, input().split()))
#     integers = list(map(int, input().split()))
    
#     integers.sort()


#     prev_minus = 0
    
#     for idx in range(num_integers-1):
#         prev_minus += (integers[idx] - prev_minus) 
    
#     target = integers[-1] - prev_minus
#     if target == target_value:
#         print("YES")
#     else:
#         print("NO")
        