#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# 324/324 cases passed (5 ms)
# Your runtime beats 80.61 % of python3 submissions
# Your memory usage beats 48.37 % of python3 submissions (21 MB)

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0
        
        while left < right:
            # We always move the pointer pointing to the smaller height
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                # Water trapped at current index is max_height - current_height
                water_trapped += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]
                
        return water_trapped
    
# @lc code=end

