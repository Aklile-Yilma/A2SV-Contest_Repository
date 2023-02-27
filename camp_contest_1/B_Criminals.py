num_test_cases = int(input())

for _ in range(num_test_cases):
    
    n = int(input())
    criminals = list(map(int, input().split()))
    operations = 0
    start_count = False
    num_zeros = 0
     
    # count zeros        
    for idx in range(n):
        num = criminals[idx]
        
        if num != 0:
            start_count = True
        if start_count and num == 0 and idx != n - 1:
            num_zeros += 1
    #calculate prefix_sum
    for idx in range(1, n):
        criminals[idx] += criminals[idx-1]
        
    operations += criminals[n-2]
    operations += num_zeros
    
    print(operations)
        
        
        
# for _ in range(num_test_cases):
    
#     n = int(input())
#     criminals = list(map(int, input().split()))
#     total = sum(criminals)
#     operations = 0
             
#     for idx in range(n):
#         num = criminals[idx]
        
#         if num != 0:
#             zero_idx = find_next_zero(criminals, idx)
#             if zero_idx == -1:
#                 continue
#             else:
#                 criminals[idx] -= 1
#                 criminals[zero_idx] += 1
#                 operations += 1
                    
#     #calculate prefix_sum
#     for idx in range(1, n):
#         criminals[idx] += criminals[idx-1]
        
#     operations += criminals[n-2]
    
#     print(operations)
        
                    
        
        