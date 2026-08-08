#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# 64/64 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 74.39 % of python3 submissions (19.2 MB)

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 1D array representing the row with 1s
        # There's only 1 way to reach any cell in the top row (always going right)
        row = [1] * n
        
        # Iterate through the grid row by row (starting from the second row)
        for i in range(1, m):
            # Update each cell in the row from left to right
            for j in range(1, n):
                # New paths to row[j] = paths from above (current row[j]) + paths from left (row[j-1])
                row[j] += row[j - 1]
                
        return row[-1]
        
# @lc code=end

