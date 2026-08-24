#
# @lc app=leetcode id=1927 lang=python3
#
# [1927] Sum Game
#
# 95/95 cases passed (56 ms)
# Your runtime beats 62.94 % of python3 submissions
# Your memory usage beats 88.24 % of python3 submissions (19.8 MB)

# @lc code=start
class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        
        left_sum = 0
        left_q = 0
        for i in range(mid):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])
                
        right_sum = 0
        right_q = 0
        for i in range(mid, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])
                
        diff_sum = left_sum - right_sum
        diff_q = right_q - left_q
        
        return diff_sum * 2 != diff_q * 9
        
# @lc code=end

