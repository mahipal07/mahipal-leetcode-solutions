#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#
# 66/66 cases passed (263 ms)
# Your runtime beats 74.29 % of python3 submissions
# Your memory usage beats 82.38 % of python3 submissions (19.6 MB)

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
            
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for i in range(1, m + 1):
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]
    
# @lc code=end

