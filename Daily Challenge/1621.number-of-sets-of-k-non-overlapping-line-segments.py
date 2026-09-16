#
# @lc app=leetcode id=1621 lang=python3
#
# [1621] Number of Sets of K Non-Overlapping Line Segments
#

# @lc code=start
import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return math.comb(n + k - 1, 2 * k) % (10**9 + 7)
        
# @lc code=end

