#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# 99/99 cases passed (114 ms)
# Your runtime beats 74.15 % of python3 submissions
# Your memory usage beats 17.1 % of python3 submissions (36.5 MB)

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = []
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))
            
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area
    
# @lc code=end

