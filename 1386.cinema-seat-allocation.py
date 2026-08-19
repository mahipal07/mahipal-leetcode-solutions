#
# @lc app=leetcode id=1386 lang=python3
#
# [1386] Cinema Seat Allocation
#
# 53/53 cases passed (23 ms)
# Your runtime beats 93.32 % of python3 submissions
# Your memory usage beats 78.41 % of python3 submissions (22.6 MB)

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(int)
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                reserved[r] |= (1 << c)
        
        ans = (n - len(reserved)) * 2
        
        left_mask = 0b0000111100  # seats 2, 3, 4, 5
        right_mask = 0b1111000000 # seats 6, 7, 8, 9
        mid_mask = 0b0011110000   # seats 4, 5, 6, 7
        
        for mask in reserved.values():
            left = (mask & left_mask) == 0
            right = (mask & right_mask) == 0
            mid = (mask & mid_mask) == 0
            
            if left and right:
                ans += 2
            elif left or right or mid:
                ans += 1
                
        return ans
       
# @lc code=end

