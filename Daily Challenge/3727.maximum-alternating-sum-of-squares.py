#
# @lc app=leetcode id=3727 lang=python3
#
# [3727] Maximum Alternating Sum of Squares
#
# 691/691 cases passed (148 ms)
# Your runtime beats 90.82 % of python3 submissions
# Your memory usage beats 49.32 % of python3 submissions (32.7 MB)

# @lc code=start
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted([x * x for x in nums])
        m = len(nums) // 2
        return sum(sq[m:]) - sum(sq[:m])
        
# @lc code=end

