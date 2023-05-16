class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # None(0) -> white(unvisited), -1 -> visited(grey), 1 -> (Black)visited and added to stack

        def dfs(sv, visited):
            # this course had not been added into the res, but visited again; there is a cycle!
            if visited[sv] == -1:
                return False
            if visited[sv] == 1:  # this course had been successfully added into the res
                return True
            # set the current course as currently being visited
            visited[sv] = -1
            for u in adj[sv]:
                if not dfs(u, visited):
                    return False  # if there is a cycle detected at any point, terminate!
            # no cycle found, dfs finished, good to add the course into the res
            res.append(sv)
            visited[sv] = 1  # this course finished
            return True

        adj = [[] for i in range(numCourses)]
        res = []
        for u, v in prerequisites:
            adj[v].append(u)
        visited = [0]*numCourses
        for i in range(numCourses):
            if not dfs(i, visited):
                # if False, there must be a cycle; terminate by returning an empty list
                return []
        return res[::-1]
