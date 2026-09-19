#
# @lc app=leetcode id=1401 lang=python3
#
# [1401] Circle and Rectangle Overlapping
#
# 90/90 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 88 % of python3 submissions (19.3 MB)

# @lc code=start
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        nearest_x = max(x1, min(xCenter, x2))
        nearest_y = max(y1, min(yCenter, y2))
        
        dx = xCenter - nearest_x
        dy = yCenter - nearest_y
        
        return dx * dx + dy * dy <= radius * radius
    
# @lc code=end

