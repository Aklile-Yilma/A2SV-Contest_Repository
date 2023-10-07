num_test_cases = int(input())

for _ in range(num_test_cases):
    num = int(input())
    candies = list(map(int, input().split()))

    min_size = min(candies)

    total = 0
    for num in candies:
        total += (num - min_size)

    print(total)