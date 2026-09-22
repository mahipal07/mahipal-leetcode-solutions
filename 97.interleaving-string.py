#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# 107/107 cases passed (3 ms)
# Your runtime beats 99.26 % of python3 submissions
# Your memory usage beats 91.22 % of python3 submissions (19.2 MB)

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
            
        if len(s1) < len(s2):
            s1, s2 = s2, s1
            
        dp = [False] * (len(s2) + 1)
        dp[0] = True
        
        for j in range(1, len(s2) + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
            
        for i in range(1, len(s1) + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, len(s2) + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
                
        return dp[len(s2)]
    
# @lc code=end

