from collections import defaultdict, deque
num_test_cases = int(input())

for _ in range(num_test_cases):
    input()
    n, k = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    indegree = [0]*n

    for _ in range(n-1):
        u, v = list(map(int, input().split()))
        u -= 1
        v -= 1
        graph[u].append(v)
        indegree[v] += 1
        graph[v].append(u)
        indegree[u] += 1

    q = deque()
    count = 0
    # append most independent nodes
    for node in range(n):
        if indegree[node] == 1 or indegree[node] == 0:
            q.append((node, 1))
            count += 1
            indegree[node] -= 1

    while q:
        node, operation = q.popleft()

        if operation == k:
            break
        # print(node, indegree)
        for child in graph[node]:
            indegree[child] -= 1
            if indegree[child] == 1 and operation < k:
                q.append((child, operation + 1))
                count += 1

        indegree[node] -= 1

    print(n - count)
