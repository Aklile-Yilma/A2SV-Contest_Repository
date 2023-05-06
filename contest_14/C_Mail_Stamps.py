from collections import defaultdict
from collections import deque

size = int(input())
graph = defaultdict(list)
for _ in range(size):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)


def findPath(graph, size):   
    path = []
    
    def bfs(node):
        nonlocal path, size
        q = deque()
        q.append(node)
        source = node
        curr_path = {node: None}
        path = []
        
        
        while q:
            node = q.popleft()
            if node != source and len(graph[node]) == 1:
                break
                
            for child in graph[node]:
                if child not in curr_path:
                    curr_path[child] = node
                    q.append(child)
                    
                    
        while node:
            path.append(node)
            node = curr_path[node]
                
        return path

    for node in graph:
        if len(graph[node]) == 1:
            return bfs(node)
        
    return []
        
path = findPath(graph, size)
print(*path)
    
    
        
        
        

    