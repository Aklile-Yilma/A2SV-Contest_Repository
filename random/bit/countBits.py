def count_onbit(num):
    count = 0

    while num != 0:
        if num % 2 != 0:
            count += 1
        
        num = num >> 1

    return count

def count_offbit(num):
    count = 0

    while num != 0:
        if num % 2 == 0:
            count += 1
        
        num = num >> 1

    return count


