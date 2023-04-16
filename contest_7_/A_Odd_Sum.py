half = int(input())
size = 2 * half
numbers = list(map(int, input().split()))

#sort in reverse
numbers.sort(reverse=True)

#first half sum
large_sum = sum(numbers[:half])
small_sum = sum(numbers[half:])

if large_sum == small_sum:
    print(-1)
else:
    print(*numbers)