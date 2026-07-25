#
# @lc app=leetcode id=3536 lang=python3
#
# [3536] Maximum Product of Two Digits
#
# 1088/1088 cases passed (4 ms)
# Your runtime beats 5.85 % of python3 submissions
# Your memory usage beats 88.69 % of python3 submissions (19.2 MB)

# @lc code=start
class Solution:
    def maxProduct(self, n: int) -> int:
        digits = sorted([int(d) for d in str(n)], reverse=True)
        return digits[0] * digits[1]
        
# @lc code=end

