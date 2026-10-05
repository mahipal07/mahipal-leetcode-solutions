#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#
# 86/86 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 97.89 % of python3 submissions (19 MB)

# @lc code=start
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0
        for i, ch in enumerate(s):
            if ch == '(':
                depth += 1
            else:
                depth -= 1
                if s[i - 1] == '(':
                    score += 1 << depth
        return score
        
# @lc code=end

