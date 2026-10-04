#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#
# 84/84 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 62.52 % of python3 submissions (19.2 MB)

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        for char in s:
            if char == "(":
                low += 1
                high += 1
            elif char == ")":
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1

            if high < 0:
                return False
            low = max(low, 0)

        return low == 0
        
# @lc code=end

