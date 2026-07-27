#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#
# 104/104 cases passed (3 ms)
# Your runtime beats 34.83 % of python3 submissions
# Your memory usage beats 68.04 % of python3 submissions (19.3 MB)

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = second = 0
        for n in nums:
            if n > first:
                second = first
                first = n
            elif n > second:
                second = n
        return (first - 1) * (second - 1)
        
# @lc code=end

