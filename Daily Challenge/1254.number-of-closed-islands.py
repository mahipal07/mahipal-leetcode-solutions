#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#
# 47/47 cases passed (13 ms)
# Your runtime beats 84.01 % of python3 submissions
# Your memory usage beats 37.84 % of python3 submissions (20 MB)

# @lc code=start
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return
            grid[r][c] = 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            if grid[r][0] == 0:
                dfs(r, 0)
            if grid[r][cols - 1] == 0:
                dfs(r, cols - 1)

        for c in range(cols):
            if grid[0][c] == 0:
                dfs(0, c)
            if grid[rows - 1][c] == 0:
                dfs(rows - 1, c)

        closed_islands = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    closed_islands += 1
                    dfs(r, c)

        return closed_islands
        
# @lc code=end

