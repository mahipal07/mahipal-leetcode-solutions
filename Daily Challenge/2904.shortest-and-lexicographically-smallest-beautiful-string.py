#
# @lc app=leetcode id=2904 lang=python3
#
# [2904] Shortest and Lexicographically Smallest Beautiful String
#
# 674/674 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 6.76 % of python3 submissions (19.5 MB)

# @lc code=start
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, ch in enumerate(s) if ch == '1']
        if len(ones) < k:
            return ""
        
        ans = ""
        for i in range(len(ones) - k + 1):
            sub = s[ones[i] : ones[i + k - 1] + 1]
            if not ans or len(sub) < len(ans) or (len(sub) == len(ans) and sub < ans):
                ans = sub
                
        return ans
       
# @lc code=end

