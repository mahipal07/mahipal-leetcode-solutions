#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :type rtype: int
        :"""
        # Sort the array to use the two-pointer technique
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            # Optimization: Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we found the exact target, return immediately
                if current_sum == target:
                    return current_sum
                
                # Update the closest sum if the current one is nearer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on the sum comparison
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum

        
# @lc code=end

