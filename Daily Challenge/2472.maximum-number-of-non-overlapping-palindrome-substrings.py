#
# @lc app=leetcode id=2472 lang=python3
#
# [2472] Maximum Number of Non-overlapping Palindrome Substrings
#
# 56/56 cases passed (10 ms)
# Your runtime beats 59.79 % of python3 submissions
# Your memory usage beats 72.68 % of python3 submissions (19.3 MB)

# @lc code=start
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        
        for i in range(k, n + 1):
            dp[i] = dp[i - 1]
            if s[i - k : i] == s[i - k : i][::-1]:
                dp[i] = max(dp[i], dp[i - k] + 1)
            if i >= k + 1 and s[i - k - 1 : i] == s[i - k - 1 : i][::-1]:
                dp[i] = max(dp[i], dp[i - k - 1] + 1)
                
        return dp[n]
    
# @lc code=end

