num = int(input())

def count_onbit(num):
    count = 0

    while num != 0:
        if num % 2 != 0:
            count += 1
        
        num = num >> 1

    return count

count = count_onbit(num)
print(count)