#
# @lc app=leetcode id=836 lang=python3
#
# [836] Rectangle Overlap
#
# 41/41 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 89.29 % of python3 submissions (19.2 MB)

# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return (
            rec1[0] < rec2[2]
            and rec2[0] < rec1[2]
            and rec1[1] < rec2[3]
            and rec2[1] < rec1[3]
        )
    
# @lc code=end

