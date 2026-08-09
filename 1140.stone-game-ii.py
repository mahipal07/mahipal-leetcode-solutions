#
# @lc app=leetcode id=1140 lang=python3
#
# [1140] Stone Game II
#
# 92/92 cases passed (166 ms)
# Your runtime beats 58.68 % of python3 submissions
# Your memory usage beats 93.18 % of python3 submissions (19.5 MB)

# @lc code=start
class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        dp = [[0] * (n + 1) for _ in range(n)]
        suffix_sum = [0] * n

        suffix_sum[n - 1] = piles[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                if i + 2 * M >= n:
                    dp[i][M] = suffix_sum[i]
                else:
                    for X in range(1, 2 * M + 1):
                        dp[i][M] = max(
                            dp[i][M],
                            suffix_sum[i] - dp[i + X][max(M, X)]
                        )

        return dp[0][1]
     
# @lc code=end

