num_test_cases = int(input())

for _ in range(num_test_cases):
    left, right = list(map(int, input().split()))

    x, y = left, left * 2

    for num in range(left, right+1):
        if num * 2 <= right:
            x = num
            y = num * 2
            break
    print(f'{x} {y}')
