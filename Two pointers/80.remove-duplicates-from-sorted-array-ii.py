#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
# 170/170 cases passed (86 ms)
# Your runtime beats 62.47 % of python3 submissions
# Your memory usage beats 46.45 % of python3 submissions (22.3 MB)

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
                
        return k
         
# @lc code=end

