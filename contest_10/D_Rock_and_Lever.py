num_test_cases = int(input())

def findBitLen(num):
    bit_len = 0
    while num != 0:
        num = num >> 1
        bit_len += 1
        
    return bit_len

for _ in range(num_test_cases):
    size = int(input())
    numbers = list(map(int, input().split()))
    result = 0
    counter = {}
    
    for num in numbers:
        bit_len = findBitLen(num)
        counter[bit_len] = counter.get(bit_len, 0) + 1
    
    for bit_len in counter:
        count = counter[bit_len]
        result += (count * (count-1))//2
        
    print(result)
        
    
        
    
            