#
# @lc app=leetcode id=3016 lang=python3
#
# [3016] Minimum Number of Pushes to Type Word II
#
# 877/877 cases passed (185 ms)
# Your runtime beats 27.43 % of python3 submissions
# Your memory usage beats 48.16 % of python3 submissions (20.1 MB)

# @lc code=start
class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26

        for c in word:
            freq[ord(c) - ord('a')] += 1

        freq.sort(reverse=True)

        totalPushes = 0
        for i in range(26):
            if freq[i] == 0:
                break
            totalPushes += freq[i] * (i // 8 + 1)

        return totalPushes

# @lc code=end

