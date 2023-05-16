from heapq import *
from typing import *
# leetcode


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)

        # append first k elements
        for idx in range(n):
            heappush(heap, (matrix[0][idx], 0, idx))

        for _ in range(k):
            min_num, row, col = heappop(heap)
            if row + 1 < n:
                heappush(heap, (matrix[row+1][col], row+1, col))

        return min_num
