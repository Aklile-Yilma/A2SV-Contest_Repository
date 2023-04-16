num_test_cases = int(input())

for _ in range(num_test_cases):
    size_a, size_b, k = list(map(int, input().split()))
    string_a = list(input())
    string_b = list(input())
    
    # sort the strings
    string_a.sort()
    string_b.sort()
    c = []
    
    ptr_1 = ptr_2 = 0
    k_a = k_b = k
        
    while ptr_1 < size_a and ptr_2 < size_b:
        
        if string_a[ptr_1] <= string_b[ptr_2] and k_a > 0 or string_a[ptr_1] >= string_b[ptr_2] and k_b <= 0:
            c.append(string_a[ptr_1])
            ptr_1 += 1
            k_a -= 1
            k_b = k
        elif k_b > 0:
            c.append(string_b[ptr_2])
            ptr_2 += 1
            k_b -= 1
            k_a = k
        elif k_b <= 0 and k_a <= 0:
            break
            
    #append remaining k   
            
    print("".join(c))    
    
    
    
    
    