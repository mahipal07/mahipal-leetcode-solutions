#
# @lc app=leetcode id=3644 lang=python3
#
# [3644] Maximum K to Sort a Permutation
#
# 822/822 cases passed (27 ms)
# Your runtime beats 79.12 % of python3 submissions
# Your memory usage beats 97.8 % of python3 submissions (31.7 MB)

# @lc code=start
class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        ans = None
        for i, x in enumerate(nums):
            if x != i:
                ans = x if ans is None else (ans & x)
        return 0 if ans is None else ans
    
# @lc code=end

