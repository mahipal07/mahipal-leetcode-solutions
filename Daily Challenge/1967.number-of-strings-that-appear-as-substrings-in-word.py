#
# @lc app=leetcode id=1967 lang=python
#
# [1967] Number of Strings That Appear as Substrings in Word
# 82/82 cases passed (0 ms)
# Your runtime beats 100 % of python submissions
# Your memory usage beats 19.82 % of python submissions (12.5 MB)

# @lc code=start
class Solution(object):
    def numOfStrings(self, patterns, word):
        return sum(1 for p in patterns if p in word)

# @lc code=end

