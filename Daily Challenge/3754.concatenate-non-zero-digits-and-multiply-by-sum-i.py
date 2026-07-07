#
# @lc app=leetcode id=3754 lang=python3
#
# [3754] Concatenate Non-Zero Digits and Multiply by Sum I
#
# 954/954 cases passed (4 ms)
# Your runtime beats 6.09 % of python3 submissions
# Your memory usage beats 51.25 % of python3 submissions (19.3 MB)

# @lc code=start
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [c for c in str(n) if c != '0']
        if not digits:
            return 0
        
        x = int("".join(digits))
        digit_sum = sum(int(d) for d in digits)
        
        return x * digit_sum
    
# @lc code=end

