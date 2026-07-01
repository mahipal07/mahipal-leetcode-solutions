#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n):
        res = []

        def backtrack(open_n, close_n, path):
            if open_n == n and close_n == n:
                res.append(path)
                return

            if open_n < n:
                backtrack(open_n + 1, close_n, path + "(")

            if close_n < open_n:
                backtrack(open_n, close_n + 1, path + ")")

        backtrack(0, 0, "")
        return res

        
# @lc code=end

