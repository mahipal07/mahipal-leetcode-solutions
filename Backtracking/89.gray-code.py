#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
# 16/16 cases passed (7 ms)
# Your runtime beats 69.99 % of python3 submissions
# Your memory usage beats 27.21 % of python3 submissions (22.6 MB)

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            res += [x | (1 << i) for x in reversed(res)]
        return res
    
# @lc code=end

