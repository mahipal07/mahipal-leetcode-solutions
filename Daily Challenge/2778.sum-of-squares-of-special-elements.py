#
# @lc app=leetcode id=2778 lang=python3
#
# [2778] Sum of Squares of Special Elements 
#
# 1437/1437 cases passed (4 ms)
# Your runtime beats 10.66 % of python3 submissions
# Your memory usage beats 14.08 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        return sum(x * x for i, x in enumerate(nums, 1) if n % i == 0)
        
# @lc code=end

