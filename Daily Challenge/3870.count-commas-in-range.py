#
# @lc app=leetcode id=3870 lang=python3
#
# [3870] Count Commas in Range
#
# 999/999 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 86.58 % of python3 submissions (19.1 MB)

# @lc code=start
class Solution:
    def countCommas(self, n: int) -> int:
        return max(0, n - 999)
    
# @lc code=end

