#
# @lc app=leetcode id=3882 lang=python3
#
# [3882] Minimum XOR Path in a Grid
#
# 999/999 cases passed (747 ms)
# Your runtime beats 69.2 % of python3 submissions
# Your memory usage beats 80.05 % of python3 submissions (25.8 MB)

# @lc code=start
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]
        dp[0] = {grid[0][0]}
        
        for j in range(1, n):
            dp[j] = {x ^ grid[0][j] for x in dp[j - 1]}
            
        for i in range(1, m):
            dp[0] = {x ^ grid[i][0] for x in dp[0]}
            for j in range(1, n):
                val = grid[i][j]
                dp[j] = {x ^ val for x in (dp[j] | dp[j - 1])}
                
        return min(dp[-1])
        
# @lc code=end

