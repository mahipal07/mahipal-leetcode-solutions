#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# 1019/1019 cases passed (3 ms)
# Your runtime beats 67.6 % of python3 submissions
# Your memory usage beats 22.63 % of python3 submissions (19.3 MB)

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
                
        return right
 
        
# @lc code=end

