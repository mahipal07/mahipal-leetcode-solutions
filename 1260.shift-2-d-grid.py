#
# @lc app=leetcode id=1260 lang=python3
#
# [1260] Shift 2D Grid
#
# 107/107 cases passed (4 ms)
# Your runtime beats 70.58 % of python3 submissions
# Your memory usage beats 19.55 % of python3 submissions (19.8 MB)

# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total
        
        flat = [val for row in grid for val in row]
        flat = flat[-k:] + flat[:-k]
        
        return [flat[i * n : (i + 1) * n] for i in range(m)]
        
# @lc code=end

