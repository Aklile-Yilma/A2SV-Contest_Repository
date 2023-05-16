n = list(input())
m = input()


def findSmallest(n):

    if n == '0':
        return 0

    # find min number != 0
    n.sort()
    for idx in range(len(n)):
        digit = n[idx]
        if digit != '0':
            n[0], n[idx] = n[idx], n[0]
            break

    return int(''.join(n))


if m[0] == '0' and len(m) > 1:
    print("WRONG_ANSWER")
elif findSmallest(n) != int(m):
    print("WRONG_ANSWER")
else:
    print('OK')
