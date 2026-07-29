#
# @lc app=leetcode id=3518 lang=python3
#
# [3518] Smallest Palindromic Rearrangement II
#
# 812/812 cases passed (1337 ms)
# Your runtime beats 28.17 % of python3 submissions
# Your memory usage beats 57.75 % of python3 submissions (19.9 MB)

# @lc code=start
from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        half = {}
        mid = ""
        m = 0
        for c in sorted(cnt):
            half[c] = cnt[c] // 2
            m += half[c]
            if cnt[c] & 1:
                mid = c

        def count(freq, rem):
            res = 1
            for c in sorted(freq):
                if freq[c]:
                    res *= comb(rem, freq[c])
                    if res >= k:
                        return res
                    rem -= freq[c]
            return res

        if count(half, m) < k:
            return ""

        left = []

        for pos in range(m):
            rem = m - pos - 1
            for c in sorted(half):
                if half[c] == 0:
                    continue

                half[c] -= 1
                ways = count(half, rem)

                if ways >= k:
                    left.append(c)
                    break

                k -= ways
                half[c] += 1

        left = "".join(left)
        return left + mid + left[::-1]
        
# @lc code=end

