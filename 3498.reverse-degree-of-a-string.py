#
# @lc app=leetcode id=3498 lang=python3
#
# [3498] Reverse Degree of a String
#

# @lc code=start
class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((ord('z') - ord(c) + 1) * i for i, c in enumerate(s, 1))
    
# @lc code=end

