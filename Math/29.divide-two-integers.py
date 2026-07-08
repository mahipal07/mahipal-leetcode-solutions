#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        negative = (dividend < 0) ^ (divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            dividend -= temp_divisor
            quotient += multiple
            
        return -quotient if negative else quotient
        
# @lc code=end

