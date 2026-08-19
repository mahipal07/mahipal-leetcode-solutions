#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# 211/211 cases passed (9 ms)
# Your runtime beats 28.2 % of python3 submissions
# Your memory usage beats 25.47 % of python3 submissions (20.9 MB)

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False
        
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
                
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
                
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
                
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
        
# @lc code=end

