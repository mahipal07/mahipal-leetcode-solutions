#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
# 103/103 cases passed (0 ms)
# Your runtime beats 100 % of python submissions
# Your memory usage beats 95.42 % of python submissions (12.4 MB)

class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
                
        return len(stack) == 0

        
# @lc code=end

