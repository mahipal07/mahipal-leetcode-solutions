#
# @lc app=leetcode id=3619 lang=python3
#
# [3619] Count Islands With Total Value Divisible by K
#
# 670/670 cases passed (287 ms)
# Your runtime beats 80.35 % of python3 submissions
# Your memory usage beats 82.11 % of python3 submissions (31.3 MB)

# @lc code=start
class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and not visited[r][c]:
                    island_sum = 0
                    stack = [(r, c)]
                    visited[r][c] = True

                    while stack:
                        curr_r, curr_c = stack.pop()
                        island_sum += grid[curr_r][curr_c]

                        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                            nr, nc = curr_r + dr, curr_c + dc
                            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] > 0:
                                visited[nr][nc] = True
                                stack.append((nr, nc))

                    if island_sum % k == 0:
                        count += 1

        return count
     
# @lc code=end

