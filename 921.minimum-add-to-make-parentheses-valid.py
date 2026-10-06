#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#
# 116/116 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 86.71 % of python3 submissions (19.2 MB)

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        add_count = 0
        for char in s:
            if char == '(':
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    add_count += 1
        return open_count + add_count
        
# @lc code=end

