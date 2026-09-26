#
# @lc app=leetcode id=1807 lang=python3
#
# [1807] Evaluate the Bracket Pairs of a String
#
# 105/105 cases passed (47 ms)
# Your runtime beats 69.16 % of python3 submissions
# Your memory usage beats 28.97 % of python3 submissions (51.9 MB)

# @lc code=start
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        res = []
        key = []
        in_bracket = False

        for char in s:
            if char == "(":
                in_bracket = True
                key = []
            elif char == ")":
                in_bracket = False
                res.append(d.get("".join(key), "?"))
            elif in_bracket:
                key.append(char)
            else:
                res.append(char)

        return "".join(res)
    
# @lc code=end

