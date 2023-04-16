n = int(input())
colors = [0]*n
colors[0] = 1
for i in range(4,n+2,2):
    colors[i-2] = 2
    
for i in range(3,n+2,2):
    if colors[i-2] != 0:
        continue
    else:
        colors[i-2] = 1
        prime = i
        i = i*i
        while i < n+2:
            colors[i-2] = 2
            i+=prime
print(len(set(colors)))
print(*colors)