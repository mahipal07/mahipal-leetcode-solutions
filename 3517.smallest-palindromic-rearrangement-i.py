#
# @lc app=leetcode id=3517 lang=python3
#
# [3517] Smallest Palindromic Rearrangement I
#
# 930/930 cases passed (308 ms)
# Your runtime beats 41.94 % of python3 submissions
# Your memory usage beats 25.81 % of python3 submissions (21.3 MB)

# @lc code=start
class Solution:

    def smallestPalindrome(self, s: str) -> str:
        half = sorted(s[: len(s) // 2])
        mid = s[len(s) // 2] if len(s) % 2 != 0 else ""
        return "".join(half) + mid + "".join(reversed(half))
        
# @lc code=end

