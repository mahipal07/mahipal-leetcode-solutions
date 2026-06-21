#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1
        x *= sign
        
        rev = 0
        while x:
            digit = x % 10
            x //= 10
            rev = rev * 10 + digit
        
        rev *= sign
        
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev


# @lc code=end

