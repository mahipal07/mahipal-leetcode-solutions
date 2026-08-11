#
# @lc app=leetcode id=2996 lang=python3
#
# [2996] Smallest Missing Integer Greater Than Sequential Prefix Sum
#
# 616/616 cases passed (1 ms)
# Your runtime beats 23 % of python3 submissions
# Your memory usage beats 17.68 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        S = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            S += nums[i]
            i += 1
        
        num_set = set(nums)
        while S in num_set:
            S += 1
            
        return S
        
# @lc code=end

