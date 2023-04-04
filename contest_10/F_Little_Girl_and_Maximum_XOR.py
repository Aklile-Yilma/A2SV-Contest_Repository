left, right = list(map(int, input().split()))

def find_bit_len(num):
    bit_len = 0
    while num != 0:
        num = num >> 1
        bit_len += 1
        
    return bit_len

num = left ^ right
count = find_bit_len(num)

print(2**count - 1)