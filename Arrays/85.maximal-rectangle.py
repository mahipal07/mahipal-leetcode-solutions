#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
# 76/76 cases passed (37 ms)
# Your runtime beats 50.02 % of python3 submissions
# Your memory usage beats 21.76 % of python3 submissions (24.6 MB)

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * (cols + 1)
        max_area = 0
        
        for row in matrix:
            for i in range(cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            
            stack = []
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
                
        return max_area
    
# @lc code=end

