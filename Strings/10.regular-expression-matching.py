#
# @lc app=leetcode id=10 lang=python
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        
        # dp[i][j] means s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # empty string matches empty pattern
        
        # Handle patterns like a*, a*b*, etc. that can match empty string
        for j in range(2, n + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    # zero occurrence
                    dp[i][j] = dp[i][j-2]
                    # one or more occurrence
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        
        return dp[m][n]


        
# @lc code=end

