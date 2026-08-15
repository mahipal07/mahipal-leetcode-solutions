#
# @lc app=leetcode id=3702 lang=python3
#
# [3702] Longest Subsequence With Non-Zero Bitwise XOR
#
# 1002/1002 cases passed (19 ms)
# Your runtime beats 92.74 % of python3 submissions
# Your memory usage beats 37.9 % of python3 submissions (33.3 MB)

# @lc code=start
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if all(x == 0 for x in nums):
            return 0
        
        total_xor = 0
        for x in nums:
            total_xor ^= x
            
        if total_xor != 0:
            return len(nums)
        
        return len(nums) - 1
        
# @lc code=end

