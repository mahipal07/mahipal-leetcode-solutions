#
# @lc app=leetcode id=3014 lang=python3
#
# [3014] Minimum Number of Pushes to Type Word I
#
# 500/500 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 16.35 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        ans = 0
        push = 1

        while n > 0:
            count = min(n, 8)
            ans += count * push
            n -= count
            push += 1

        return ans

# @lc code=end

