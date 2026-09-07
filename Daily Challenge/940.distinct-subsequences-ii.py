#
# @lc app=leetcode id=940 lang=python3
#
# [940] Distinct Subsequences II
#
# 110/110 cases passed (10 ms)
# Your runtime beats 66.67 % of python3 submissions
# Your memory usage beats 91.67 % of python3 submissions (19.2 MB)

# @lc code=start
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        last = [0] * 26

        for ch in s:
            idx = ord(ch) - ord("a")
            added = (total + 1 - last[idx]) % MOD
            total = (total + added) % MOD
            last[idx] = (last[idx] + added) % MOD

        return total
        
# @lc code=end

