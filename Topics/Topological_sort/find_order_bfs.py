from collections import defaultdict
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # build graph and indegree
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        q = deque()
        visited = set()
        order = []
        # append independent node to the queue
        for node in range(len(indegree)):
            if indegree[node] == 0:
                q.append(node)
                visited.add(node)

        while q:
            node = q.popleft()
            order.append(node)

            for child in graph[node]:
                if child not in visited:
                    # decrement indegree of children
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        # append independent child
                        q.append(child)
                        visited.add(child)
        # if there is a cycle return false
        if len(visited) < numCourses:
            return []

        return order
