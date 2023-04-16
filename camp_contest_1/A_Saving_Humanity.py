num_test_cases = int(input())

for _ in range(num_test_cases):
    n , m = list(map(int, input().split()))
    soldiers = list(input())
    soldiers.insert(0, '0')
    soldiers.append('0')
    
    isChanged = True
    while isChanged and m > 0:
        indices = []
        for idx in range(1, len(soldiers)-1):
            before = soldiers[idx-1]
            curr = soldiers[idx]
            after = soldiers[idx+1]
            
            if curr == '0':
                if before == '0' and after == '1':
                    indices.append(idx)
                elif before == '1' and after == '0':
                    indices.append(idx)
                
        if indices:
            for idx in indices:
                soldiers[idx] = '1'
        else:
            isChanged = False
        
        m -= 1
        
    soldiers = soldiers[1:len(soldiers)-1]
    print(''.join(soldiers))
        
    
    
    

