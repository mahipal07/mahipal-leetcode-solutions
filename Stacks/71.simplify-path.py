#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#
# 265/265 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 90.98 % of python3 submissions (19.2 MB)

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")
        
        for part in parts:
            if part == "" or part == ".":
                continue
            if part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
                
        return "/" + "/".join(stack)
        
# @lc code=end

