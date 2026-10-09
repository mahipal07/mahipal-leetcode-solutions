#
# @lc app=leetcode id=1541 lang=python3
#
# [1541] Minimum Insertions to Balance a Parentheses String
#
# 102/102 cases passed (71 ms)
# Your runtime beats 57.89 % of python3 submissions
# Your memory usage beats 59.3 % of python3 submissions (19.8 MB)

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_needed = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == "(":
                open_needed += 1
                i += 1
            else:
                if i + 1 < n and s[i + 1] == ")":
                    i += 2
                else:
                    insertions += 1
                    i += 1

                if open_needed > 0:
                    open_needed -= 1
                else:
                    insertions += 1

        insertions += open_needed * 2
        return insertions
        
# @lc code=end

