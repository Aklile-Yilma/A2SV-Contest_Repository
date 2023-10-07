from collections import defaultdict
import heapq
num_cities, num_roads, num_routes = map(int, input().split())

graph = defaultdict(list)

for _ in range(num_roads):
    src, dst, weight = map(int, input().split())
    graph[src].append((dst, weight, 'r'))
    # graph[dst].append((src, weight, 'r'))

src = 1
ans = num_routes
train_routes = defaultdict(int)
for _ in range(num_routes):
    dst, weight = map(int, input().split())
    graph[src].append((dst, weight, 't'))
    # graph[dst].append((src, weight, 't'))

#diakestra's algorithm

distance = [float('inf')] * (num_cities + 1)
visited = set()
heap = []
#init, weight, node, type
heapq.heappush(heap, (0, 1, 'r'))

# print(graph)
while heap:
    # print(heap)
    curr_weight, node, route_type = heapq.heappop(heap)
    if distance[node] == float('inf') or distance[node][0] > curr_weight:
        distance[node] = (curr_weight, node, route_type)

    if (node, route_type) in visited:
        continue

    visited.add((node, route_type))

    for neighbor, weight, n_route_type in graph[node]:
        new_weight = curr_weight + weight
        if distance[neighbor] != float('inf') and distance[neighbor][0] < new_weight:
            continue 

        heapq.heappush(heap, (curr_weight + weight, neighbor, n_route_type))


distance = distance[1:]
for weight, node, route_type in distance:
    if route_type == 't':
        ans -= 1

print(ans)
        
