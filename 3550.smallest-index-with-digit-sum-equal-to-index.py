#
# @lc app=leetcode id=3550 lang=python3
#
# [3550] Smallest Index With Digit Sum Equal to Index
#
# 982/982 cases passed (2 ms)
# Your runtime beats 65.51 % of python3 submissions
# Your memory usage beats 93.24 % of python3 submissions (19.2 MB)

# @lc code=start
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, val in enumerate(nums):
            if sum(int(d) for d in str(val)) == i:
                return i
        return -1
    
# @lc code=end

