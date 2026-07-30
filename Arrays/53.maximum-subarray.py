#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# 210/210 cases passed (40 ms)
# Your runtime beats 40.32 % of python3 submissions
# Your memory usage beats 43.44 % of python3 submissions (31.4 MB)

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        current_max = nums[0]
        
        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            max_so_far = max(max_so_far, current_max)
            
        return max_so_far
          
# @lc code=end

