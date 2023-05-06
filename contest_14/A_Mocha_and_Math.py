num_test_cases = int(input())

for _ in range(num_test_cases):
    size = int(input())
    numbers = list(map(int, input().split()))
    total = numbers[0]
    for num in numbers:
        total &= num
        
    print(total)
    
    