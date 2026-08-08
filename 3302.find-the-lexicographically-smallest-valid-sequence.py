#
# @lc app=leetcode id=3302 lang=python3
#
# [3302] Find the Lexicographically Smallest Valid Sequence
#
# 905/905 cases passed (364 ms)
# Your runtime beats 91.3 % of python3 submissions
# Your memory usage beats 67.39 % of python3 submissions (47.4 MB)

# @lc code=start
class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)

        ans = [0] * m
        last = [-1] * m

        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1

        j = 0
        canSkip = True

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans[j] = i
                j += 1
            elif canSkip and (j == m - 1 or i < last[j + 1]):
                ans[j] = i
                j += 1
                canSkip = False

        return ans if j == m else []
        
# @lc code=end

