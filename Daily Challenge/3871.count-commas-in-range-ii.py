#
# @lc app=leetcode id=3871 lang=python3
#
# [3871] Count Commas in Range II
#
# 1100/1100 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 87.75 % of python3 submissions (19.2 MB)

# @lc code=start
class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        threshold = 1000
        
        # Each threshold of 10^(3k) adds 1 extra comma for all numbers >= threshold
        while threshold <= n:
            total_commas += n - threshold + 1
            threshold *= 1000
            
        return total_commas
        
# @lc code=end

