#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# 45/45 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 52.41 % of python3 submissions (19.2 MB)

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        first, second = 1, 2
        for _ in range(3, n + 1):
            first, second = second, first + second
            
        return second
    
# @lc code=end

