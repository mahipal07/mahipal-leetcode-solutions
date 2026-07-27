#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# 307/307 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 18.95 % of python3 submissions (19.6 MB)

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if n < 0:
            x = 1 / x
            n = -n
            
        res = 1.0
        while n > 0:
            if n % 2 == 1:
                res *= x
            x *= x
            n //= 2
            
        return res
    
# @lc code=end

