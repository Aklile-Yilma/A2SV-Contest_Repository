from collections import defaultdict

    
n = int(input())
graph = defaultdict(int)
for node in range(1, n+1):
    curr_parent = int(input())
    graph[node] = curr_parent

print(graph)
groups = [set() for _ in range(n)]
for node in graph:
    idx = 0
    while idx < n:            
        if graph[node] not in groups[idx]:
            groups[idx].add(node)
            break
        
print(len(groups))
        


    


