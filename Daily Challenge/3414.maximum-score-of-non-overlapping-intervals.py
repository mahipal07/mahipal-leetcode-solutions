#
# @lc app=leetcode id=3414 lang=python3
#
# [3414] Maximum Score of Non-overlapping Intervals
#
# 581/581 cases passed (1497 ms)
# Your runtime beats 61.02 % of python3 submissions
# Your memory usage beats 50.85 % of python3 submissions (80.9 MB)

# @lc code=start
from bisect import bisect_left


class Solution:

    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        events = sorted(
            (r, l, w, i) for i, (l, r, w) in enumerate(intervals)
        )
        r_list = [e[0] for e in events]
        n = len(events)

        dp = [[(0, []) for _ in range(n + 1)] for _ in range(5)]

        for j in range(1, n + 1):
            r, l, w, idx = events[j - 1]
            p = bisect_left(r_list, l)

            for k in range(1, 5):
                best = dp[k][j - 1]

                prev_w, prev_indices = dp[k - 1][p]
                cand_w = prev_w + w
                cand_indices = sorted(prev_indices + [idx])

                if cand_w > best[0]:
                    best = (cand_w, cand_indices)
                elif cand_w == best[0] and (
                    not best[1] or cand_indices < best[1]
                ):
                    best = (cand_w, cand_indices)

                dp[k][j] = best

        ans_w, ans_indices = 0, []
        for k in range(1, 5):
            w, indices = dp[k][n]
            if w > ans_w:
                ans_w, ans_indices = w, indices
            elif w == ans_w and indices and (not ans_indices or indices < ans_indices):
                ans_indices = indices

        return ans_indices
    
# @lc code=end

