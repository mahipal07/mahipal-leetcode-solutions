#
# @lc app=leetcode id=3622 lang=python3
#
# [3622] Check Divisibility by Digit Sum and Product
#
# 636/636 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 65.51 % of python3 submissions (19.3 MB)

# @lc code=start
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1
        for d in str(n):
            digit = int(d)
            digit_sum += digit
            digit_product *= digit
        return n % (digit_sum + digit_product) == 0
        
# @lc code=end

