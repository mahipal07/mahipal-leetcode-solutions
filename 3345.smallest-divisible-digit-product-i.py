#
# @lc app=leetcode id=3345 lang=python3
#
# [3345] Smallest Divisible Digit Product I
#
# 1000/1000 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 32.93 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            prod = 1
            temp = n

            while temp > 0:
                prod *= temp % 10
                temp //= 10

            if prod % t == 0:
                return n

            n += 1

# @lc code=end

