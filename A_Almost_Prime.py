def prime_factorization(num):
    factors = []
    d = 2
    while d * d <= num:
        while num % d == 0:
            factors.append(d)
            num = num // d
        d+=1
        
    if num > 1:
        factors.append(num)
        
    return factors

n = int(input())
count = 0
for num in range(n+1):
    factors = prime_factorization(num)
    if len(set(factors)) == 2:
        count += 1
        
print(count)
        
    
    
    
    