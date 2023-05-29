num_test_cases = int(input())


def count(n, start):
    count = len(n) - start - 1
    for i in range(start-1, -1, -1):
        # find the other o or 5
        if n[start] == '0':
            if n[i] == '0' or n[i] == '5':
                break

        # if start is 5 find 7 0r 2
        if n[start] == '5':
            if n[i] == '7' or n[i] == '2':
                break
        count += 1

    return count


for _ in range(num_test_cases):
    n = list(input())

    zero_start = -1
    five_start = -1
    # find first valid
    for i in range(len(n)-1, -1, -1):
        curr = n[i]
        if curr == '5':
            five_start = i
            break
    for i in range(len(n)-1, -1, -1):
        curr = n[i]
        if curr == '0':
            zero_start = i
            break

    c = float('inf')
    if five_start != -1:
        c = min(c, count(n, five_start))
    if zero_start != -1:
        c = min(c, count(n, zero_start))

    print(c)
