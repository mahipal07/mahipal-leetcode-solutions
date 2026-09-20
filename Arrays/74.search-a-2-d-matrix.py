#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# 133/133 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 39.41 % of python3 submissions (19.5 MB)

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        
        while low <= high:
            mid = (low + high) // 2
            mid_val = matrix[mid // n][mid % n]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False
 
# @lc code=end

