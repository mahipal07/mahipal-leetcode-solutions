#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#
# 1499/1499 cases passed (7 ms)
# Your runtime beats 3.02 % of python3 submissions
# Your memory usage beats 9.63 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_exponent = False
        seen_dot = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in ('+', '-'):
                if i > 0 and s[i - 1] not in ('e', 'E'):
                    return False
            elif char in ('e', 'E'):
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif char == '.':
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False
                
        return seen_digit
 
        
# @lc code=end

