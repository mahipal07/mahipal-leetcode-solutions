#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# 60/60 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 15.75 % of python3 submissions (19.5 MB)

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if not words:
            return 0
        return len(words[-1])
    
# @lc code=end

