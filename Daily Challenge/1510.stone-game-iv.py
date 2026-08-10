#
# @lc app=leetcode id=1510 lang=python3
#
# [1510] Stone Game IV
#
# 72/72 cases passed (582 ms)
# Your runtime beats 65.15 % of python3 submissions
# Your memory usage beats 96.67 % of python3 submissions (19.8 MB)

# @lc code=start
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            k = 1
            while k * k <= i:
                if not dp[i - k * k]:
                    dp[i] = True
                    break
                k += 1

        return dp[n]
    
# @lc code=end

