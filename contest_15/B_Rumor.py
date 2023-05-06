from collections import defaultdict
from collections import deque
n, m = list(map(int, input().split()))
coins = list(map(int, input().split()))

graph = defaultdict(list)
for _ in range(m):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)
    
def bfs(root):
    q = deque()
    q.append(root)
    visited= {root}
    total = coins[root-1]
    
    while q:
        node = q.popleft()
        
        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                q.append(child)
                
    for idx in range(len(coins)):
        if (idx + 1) not in visited:
            total += coins[idx]
            
    return total
                
coin_spent = sum(coins)
print(graph)
for node in graph:
    coin_spent = min(coin_spent, bfs(node))
    
    
print(coin_spent)
    
