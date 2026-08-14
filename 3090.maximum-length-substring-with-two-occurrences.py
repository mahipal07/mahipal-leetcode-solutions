#
# @lc app=leetcode id=3090 lang=python3
#
# [3090] Maximum Length Substring With Two Occurrences
#
# 709/709 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 21.08 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        count = [0] * 26

        for right in range(len(s)):
            count[ord(s[right]) - ord('a')] += 1

            while count[ord(s[right]) - ord('a')] > 2:
                count[ord(s[left]) - ord('a')] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
    
# @lc code=end

