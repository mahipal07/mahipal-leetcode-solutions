#
# @lc app=leetcode id=2029 lang=python3
#
# [2029] Stone Game IX
#
# 106/106 cases passed (47 ms)
# Your runtime beats 72.52 % of python3 submissions
# Your memory usage beats 96.95 % of python3 submissions (30.3 MB)

# @lc code=start
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        c = [0] * 3
        for x in stones:
            c[x % 3] += 1
        
        if c[0] % 2 == 0:
            return c[1] > 0 and c[2] > 0
        return abs(c[1] - c[2]) > 2
        
# @lc code=end

