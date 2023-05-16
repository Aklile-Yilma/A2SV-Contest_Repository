import collections

n, m = [int(x) for x in input().split()]
edges = []
graph = collections.defaultdict(set)
for _ in range(m):
    l, r = [int(x) for x in input().split()]
    graph[l].add(r)
    graph[r].add(l)
    edges.append([l, r])

root = list(graph.keys())[0]
state = True
stack = [[root, True]]
labels = {}
visited = set([root])
brocken = False
while stack:
    curr, state = stack.pop()
    for n in graph[curr]:
        if (curr, n) in labels:
            if labels[(curr, n)] and state:
                continue
            if not labels[(curr, n)] and not state:
                continue
            else:
                print('NO')
                brocken = True
                break
        else:
            labels[(curr, n)] = state
            labels[(n, curr)] = not state
        if n in visited:
            continue

        stack.append([n, not state])
        visited.add(n)
    if brocken:
        break
ans = []
if not brocken:
    print('YES')
    for l, r in edges:
        if labels[(l, r)]:
            ans.append('1')
        else:
            ans.append('0')

    print("".join(ans))
