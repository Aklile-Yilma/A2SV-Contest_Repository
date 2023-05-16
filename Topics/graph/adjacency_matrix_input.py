from collections import defaultdict
# take adjacency matrix input
graph = defaultdict(list)

for row in range(n):
    line = list(map(int, input().split()))
    size = len(line)
    
    for col in range(size):
        if line[col] == 1:
            graph[row+1].append(col+1)
    
    # if not graph[row+1]:
    #     graph[row+1] = []