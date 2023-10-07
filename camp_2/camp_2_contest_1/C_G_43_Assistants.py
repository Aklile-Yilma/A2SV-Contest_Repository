
t = int(input())
for _ in range(t):
    n = int(input())
    q = []
    _max = 0
    for line in range(n):
        start, end = map(int, input().split())
        _max = max(_max, end)
        q.append((start, end))


    pref = [0]*(_max + 1)

    for start, end in q:
        pref[start] += 1
        pref[end] -= 1

    # running sum
    for ind in range(1, _max + 1):
        pref[ind] += pref[ind - 1]
    

    print(max(pref))

