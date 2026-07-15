#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#
# 85/85 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 8.31 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        n, m = len(haystack), len(needle)
        
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        
        return -1
        
# @lc code=end

