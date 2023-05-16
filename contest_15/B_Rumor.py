from collections import defaultdict, deque
 
 
n, m = map(int, input().split())
 
nums = list(map(int, input().split()))
adj = defaultdict(list)
seen = set()
 
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
 
 
def bfs(num):
    q = deque()
    min_price = nums[num-1]
    q.append(num)
 
    while q:
        val = q.popleft()
        seen.add(val)
 
        for ad in adj[val]:
            if ad not in seen:
                q.append(ad)
            seen.add(ad)
            min_price = min(min_price, nums[ad-1])
 
    return min_price
 
 
total = 0
 
for i in range(1, n+1):
    if i not in seen:
        total += bfs(i)
 
print(total)