#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#
# 93/93 cases passed (27 ms)
# Your runtime beats 15.14 % of python3 submissions
# Your memory usage beats 42.28 % of python3 submissions (20.4 MB)

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
      
# @lc code=end

