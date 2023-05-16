from collections import defaultdict
n = int(input())
matrix = []

for row in range(n):
    matrix.append(list(map(int, input().split())))
    

#sources all column values are zero
sources = []
for col in range(n):
    total = 0
    for row in range(n):
        total += matrix[row][col]
    if total == 0:
        sources.append(col+1)
    
#sink- all row values are zero 
sinks = []
for row in range(n):
    if sum(matrix[row]) == 0:
        sinks.append(row+1)

print(len(sources), *sources)
print(len(sinks), *sinks)     

# take adjacency matrix input
# graph = defaultdict(list)

# def add_remove(sources, source):
#     if source not in visited:
#         sources.add(source)
#     else:
#         if source in sources:
#             sources.remove(source)
    

# for row in range(n):
#     line = list(map(int, input().split()))
#     size = len(line)
    
#     for col in range(size):
#         if line[col] == 1:
#             graph[row+1].append(col+1)
    
#     if not graph[row+1]:
#         graph[row+1] = []
        
   
# print(graph)         
# for source in graph:
#     children = graph[source]
#     for child in children:
#         if graph.get(child, []) == []:
#             sinks.append(child)
        
#         if child in sources:
#             sources.remove(child)
        
#         visited.add(child)
        
#     add_remove(sources, source)
#     if graph.get(source, []) == []:
#         sinks.append(source)
#     visited.add(source)
        
# print(len(sources), *list(sources))
# print(len(sinks), *sinks)        


    
    
            
        
        
    
    