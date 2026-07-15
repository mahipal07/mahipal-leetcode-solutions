#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# 66/66 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 11.09 % of python3 submissions (20.1 MB)

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return low
        
# @lc code=end

