#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
# Accepted
# 285/285 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 94.99 % of python3 submissions (19.5 MB)

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return True
                
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
                
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return False
        
# @lc code=end

