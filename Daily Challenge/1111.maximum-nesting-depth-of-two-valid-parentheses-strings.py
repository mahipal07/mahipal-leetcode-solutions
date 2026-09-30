#
# @lc app=leetcode id=1111 lang=python3
#
# [1111] Maximum Nesting Depth of Two Valid Parentheses Strings
#
# 31/31 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 63.43 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        depth = 0
        for ch in seq:
            if ch == "(":
                depth += 1
                res.append(depth % 2)
            else:
                res.append(depth % 2)
                depth -= 1
        return res
    
# @lc code=end

