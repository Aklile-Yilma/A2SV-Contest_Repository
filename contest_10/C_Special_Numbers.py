num_test_cases = int(input())
MOD = (10**9)+7

for _ in range(num_test_cases):
    n, k = list(map(int, input().split()))

    result = 0
    num = k
    idx = 0
    while num != 0:
        if num % 2 != 0:
            result += (n ** idx)
        num = num >> 1
        idx += 1
        
    print(result % MOD)
        
