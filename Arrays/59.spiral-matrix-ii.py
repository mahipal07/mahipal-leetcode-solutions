#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
# 20/20 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 42.05 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize an n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Define boundaries
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        
        num = 1
        
        while top <= bottom and left <= right:
            # Move right across the top row
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            
            # Move down the right column
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            
            # Move left across the bottom row
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            
            # Move up the left column
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            
        return matrix
         
# @lc code=end

