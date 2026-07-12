#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# 196/196 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 77.75 % of python3 submissions (19.3 MB)

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            
            # Identify which half is sorted
            if nums[low] <= nums[mid]:
                # Left half is sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return -1
        
# @lc code=end

