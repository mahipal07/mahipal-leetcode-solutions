#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# 8/8 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 36.93 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(open_n, closed_n, current_str):
            if open_n == closed_n == n:
                res.append(current_str)
                return

            if open_n < n:
                backtrack(open_n + 1, closed_n, current_str + "(")

            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, current_str + ")")

        backtrack(0, 0, "")
        return res
     
# @lc code=end

