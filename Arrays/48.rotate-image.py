#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# 21/21 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 27.79 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for row in matrix:
            row.reverse()
        """
        Do not return anything, modify matrix in-place instead.
        """
        
# @lc code=end

