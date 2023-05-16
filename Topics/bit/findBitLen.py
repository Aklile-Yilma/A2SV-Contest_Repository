def findBitLen(num):
    bit_len = 0
    while num != 0:
        num = num >> 1
        bit_len += 1
        
    return bit_len
