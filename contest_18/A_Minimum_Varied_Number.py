num_test_cases = int(input())


for _ in range(num_test_cases):
    num = int(input())
    stack = []
    count = 0
    for i in range(9, 0, -1):
        if num - i >= 0:
            stack.append(str(i))
            num -= i

    stack.reverse()
    print(''.join(stack))
