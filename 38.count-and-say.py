#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
# 30/30 cases passed (8 ms)
# Your runtime beats 32.87 % of python3 submissions
# Your memory usage beats 36.49 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        for _ in range(n - 1):
            res = []
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                res.append(str(j - i))
                res.append(s[i])
                i = j
            s = "".join(res)

        return s
        
# @lc code=end

