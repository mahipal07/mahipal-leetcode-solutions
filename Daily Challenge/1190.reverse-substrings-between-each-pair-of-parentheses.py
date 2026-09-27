#
# @lc app=leetcode id=1190 lang=python3
#
# [1190] Reverse Substrings Between Each Pair of Parentheses
#
# 40/40 cases passed (11 ms)
# Your runtime beats 40.15 % of python3 submissions
# Your memory usage beats 29.73 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                sub = []
                while stack and stack[-1] != '(':
                    sub.append(stack.pop())
                stack.pop()
                stack.extend(sub)
            else:
                stack.append(char)
        return "".join(stack)
    
# @lc code=end

