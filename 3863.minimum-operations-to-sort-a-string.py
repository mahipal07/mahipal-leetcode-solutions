#
# @lc app=leetcode id=3863 lang=python3
#
# [3863] Minimum Operations to Sort a String
#
# 1291/1291 cases passed (254 ms)
# Your runtime beats 32.8 % of python3 submissions
# Your memory usage beats 13.6 % of python3 submissions (21.3 MB)

# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        if list(s) == sorted(s):
            return 0
        if len(s) == 2:
            return -1

        min_char = min(s)
        max_char = max(s)

        if s[0] == min_char or s[-1] == max_char:
            return 1

        if (
            s[0] == max_char
            and s[-1] == min_char
            and s.count(max_char) == 1
            and s.count(min_char) == 1
        ):
            return 3

        return 2
        
# @lc code=end

