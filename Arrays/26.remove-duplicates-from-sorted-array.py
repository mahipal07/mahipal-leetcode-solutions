#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
# 362/362 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 78.16 % of python3 submissions (20.4 MB)

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k
        
# @lc code=end

