#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        start = 0
        max_len = 0

        for i, ch in enumerate(s):
            if ch in last_index and last_index[ch] >= start:
                start = last_index[ch] + 1
            last_index[ch] = i
            max_len = max(max_len, i - start + 1)

        return max_len

# @lc code=end

