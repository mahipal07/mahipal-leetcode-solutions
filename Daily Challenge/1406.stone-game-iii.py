#
# @lc app=leetcode id=1406 lang=python3
#
# [1406] Stone Game III
#

# @lc code=start
from typing import List
from functools import lru_cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0

            best = float("-inf")
            take = 0
            for j in range(i, min(i + 3, n)):
                take += stoneValue[j]
                best = max(best, take - dp(j + 1))
            return best

        score = dp(0)

        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"
       
# @lc code=end

