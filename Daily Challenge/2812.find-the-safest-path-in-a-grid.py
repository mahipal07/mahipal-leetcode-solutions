#
# @lc app=leetcode id=2812 lang=python
#
# [2812] Find the Safest Path in a Grid
#

# @lc code=start
import heapq
from collections import deque


class Solution(object):

    def maximumSafenessFactor(self, grid):
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0

        dist = [[float("inf")] * n for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float("inf"):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        max_heap = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while max_heap:
            d, r, c = heapq.heappop(max_heap)
            d = -d

            if r == n - 1 and c == n - 1:
                return d

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(max_heap, (-min(d, dist[nr][nc]), nr, nc))

        return 0

        
# @lc code=end

