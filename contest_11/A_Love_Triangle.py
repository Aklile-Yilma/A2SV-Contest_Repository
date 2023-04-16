from collections import defaultdict
n = int(input())
planes = list(map(int, input().split()))
graph = defaultdict(int)

for idx in range(n):
    graph[idx+1] = planes[idx]

def check(graph):
    for idx in range(n):                  
        if graph[graph[graph[idx+1]]] == idx+1:
            return True
    return False

if check(graph):
    print("YES")
else:
    print("NO")
    