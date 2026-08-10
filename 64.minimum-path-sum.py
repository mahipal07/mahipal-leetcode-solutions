#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# 66/66 cases passed (11 ms)
# Your runtime beats 54.9 % of python3 submissions
# Your memory usage beats 83.56 % of python3 submissions (21.2 MB)

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        # 1. Fill out the first row (can only come from the left)
        for c in range(1, COLS):
            grid[0][c] += grid[0][c-1]
            
        # 2. Fill out the first column (can only come from above)
        for r in range(1, ROWS):
            grid[r][0] += grid[r-1][0]
            
        # 3. Fill out the rest of the grid
        for r in range(1, ROWS):
            for c in range(1, COLS):
                grid[r][c] += min(grid[r-1][c], grid[r][c-1])
                
        # The bottom-right corner holds the total minimum path sum
        return grid[-1][-1]
    
# @lc code=end

