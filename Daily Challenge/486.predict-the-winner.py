#
# @lc app=leetcode id=486 lang=python3
#
# [486] Predict the Winner
#
# 62/62 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 42.77 % of python3 submissions (19.5 MB)

# @lc code=start
from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:]  # Copy of nums

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[-1] >= 0
    
# @lc code=end

