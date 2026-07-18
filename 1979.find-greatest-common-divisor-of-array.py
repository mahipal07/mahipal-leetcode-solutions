#
# @lc app=leetcode id=1979 lang=python3
#
# [1979] Find Greatest Common Divisor of Array
#
# 215/215 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 42.65 % of python3 submissions (19.3 MB)

# @lc code=start
import math
from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return math.gcd(min(nums), max(nums))
    
# @lc code=end

