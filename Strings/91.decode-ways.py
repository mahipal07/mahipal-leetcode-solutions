#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# 269/269 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 22.42 % of python3 submissions (19.5 MB)

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        prev2 = 1
        prev1 = 1
        
        for i in range(1, len(s)):
            current = 0
            if s[i] != '0':
                current += prev1
                
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2
                
            prev2 = prev1
            prev1 = current
            
            if prev1 == 0:
                return 0
                
        return prev1
        
# @lc code=end

