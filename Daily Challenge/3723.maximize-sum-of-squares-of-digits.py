#
# @lc app=leetcode id=3723 lang=python3
#
# [3723] Maximize Sum of Squares of Digits
#
# 1000/1000 cases passed (39 ms)
# Your runtime beats 53.32 % of python3 submissions
# Your memory usage beats 38.06 % of python3 submissions (22 MB)

# @lc code=start
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        
        q, r = divmod(sum, 9)
        ans = ["9"] * q
        if r > 0:
            ans.append(str(r))
        ans.append("0" * (num - len(ans)))
        
        return "".join(ans)
     
# @lc code=end

