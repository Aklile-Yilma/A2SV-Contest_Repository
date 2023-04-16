num_test_cases = int(input())


for _ in range(num_test_cases):
    size = int(input())
    arr = list(map(int, input().split()))
    max_sum = 0
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j or arr[j] % 2 != 0:
                continue
            else:
                while arr[j]%2 == 0:
                    arr[j] //= 2
                    arr[i] *= 2
        max_sum = max(max_sum, sum(arr))
        
    print(max_sum)
    