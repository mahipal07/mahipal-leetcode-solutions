#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#
# 168/168 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 50.4 % of python3 submissions (19.2 MB)

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        max_d = curr = 0
        for ch in s:
            if ch == "(":
                curr += 1
                if curr > max_d:
                    max_d = curr
            elif ch == ")":
                curr -= 1
        return max_d
        
# @lc code=end

