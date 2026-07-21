#
# @lc app=leetcode id=3499 lang=python3
#
# [3499] Maximize Active Section with Trade I
#
# 996/996 cases passed (468 ms)
# Your runtime beats 95.33 % of python3 submissions
# Your memory usage beats 65.42 % of python3 submissions (21 MB)

# @lc code=start
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        zero_blocks = []
        ones_count = 0
        
        curr_zero = 0
        for char in s:
            if char == '1':
                ones_count += 1
                if curr_zero > 0:
                    zero_blocks.append(curr_zero)
                    curr_zero = 0
            else:
                curr_zero += 1
        if curr_zero > 0:
            zero_blocks.append(curr_zero)
            
        max_gain = 0
        for i in range(len(zero_blocks) - 1):
            max_gain = max(max_gain, zero_blocks[i] + zero_blocks[i + 1])
            
        return ones_count + max_gain
    
# @lc code=end

