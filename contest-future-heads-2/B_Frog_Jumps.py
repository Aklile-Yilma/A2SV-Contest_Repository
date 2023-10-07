import math
num_test_cases = int(input())
for _ in range(num_test_cases):
    board = input()
    size = len(board)

    d = 1
    num_R = 0
    num_L = 0

    for item in board:
        if item == 'R':
            num_R += 1
        else:
            num_L += 1

    if num_R > 0 and num_L > 0:
        d = math.ceil((num_R + num_L) / num_R)
    elif num_R == 0:
        d = num_L + 1
    else:
        d = 1

    print(d)
    