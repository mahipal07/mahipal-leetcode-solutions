#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# 90/90 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 62.37 % of python3 submissions (19.3 MB)

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# @lc code=end

