#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
# 42/42 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 31.24 % of python3 submissions (19.5 MB)

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1
        
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c > 0:
                    dp[c] += dp[c - 1]
                    
        return dp[-1]
          
# @lc code=end

