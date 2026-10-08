#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#
# 59/59 cases passed (3 ms)
# Your runtime beats 64.63 % of python3 submissions
# Your memory usage beats 32.26 % of python3 submissions (19.3 MB)

# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        depth = 0
        for ch in s:
            if ch == '(':
                if depth > 0:
                    res.append(ch)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    res.append(ch)
        return "".join(res)
        
# @lc code=end

