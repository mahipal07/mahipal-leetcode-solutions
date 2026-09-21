#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# 19/19 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 89.85 % of python3 submissions (19.2 MB)

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        c = 1
        for i in range(1, n + 1):
            c = c * 2 * (2 * i - 1) // (i + 1)
        return c
        
# @lc code=end

