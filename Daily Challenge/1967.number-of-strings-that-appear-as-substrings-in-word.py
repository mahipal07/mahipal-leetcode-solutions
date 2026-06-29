#
# @lc app=leetcode id=1967 lang=python
#
# [1967] Number of Strings That Appear as Substrings in Word
#

# @lc code=start
class Solution(object):
    def numOfStrings(self, patterns, word):
        return sum(1 for p in patterns if p in word)

# @lc code=end

