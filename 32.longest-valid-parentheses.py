#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# 235/235 cases passed (7 ms)
# Your runtime beats 90.33 % of python3 submissions
# Your memory usage beats 39.73 % of python3 submissions (20.6 MB)

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len
        
# @lc code=end

