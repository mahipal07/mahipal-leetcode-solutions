#
# @lc app=leetcode id=1658 lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
#
# 97/97 cases passed (67 ms)
# Your runtime beats 80.96 % of python3 submissions
# Your memory usage beats 26.53 % of python3 submissions (31.4 MB)

# @lc code=start
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        
        max_len = -1
        current_sum = 0
        left = 0
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        return len(nums) - max_len if max_len != -1 else -1
        
# @lc code=end

