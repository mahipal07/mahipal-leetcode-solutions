#
# @lc app=leetcode id=3876 lang=python3
#
# [3876] Construct Uniform Parity Array II
#

# @lc code=start
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return min(nums1) % 2 == 1 or all(x % 2 == 0 for x in nums1)
        
# @lc code=end

