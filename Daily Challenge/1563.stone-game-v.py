#
# @lc app=leetcode id=1563 lang=python3
#
# [1563] Stone Game V
#

# @lc code=start
# 132/132 cases passed (2105 ms)
# Your runtime beats 58.82 % of python3 submissions
# Your memory usage beats 57.65 % of python3 submissions (36.9 MB)

from typing import List


class Solution:

    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]

        memo = [[0] * n for _ in range(n)]

        def solve(i: int, j: int) -> int:
            if i == j:
                return 0
            if memo[i][j]:
                return memo[i][j]

            ans = 0
            total = pref[j + 1] - pref[i]

            for k in range(i, j):
                left = pref[k + 1] - pref[i]
                right = total - left

                if left < right:
                    if ans >= 2 * left:
                        continue
                    ans = max(ans, left + solve(i, k))
                elif left > right:
                    if ans >= 2 * right:
                        break
                    ans = max(ans, right + solve(k + 1, j))
                else:
                    ans = max(ans, left + max(solve(i, k), solve(k + 1, j)))

            memo[i][j] = ans
            return ans

        return solve(0, n - 1)
        
# @lc code=end

