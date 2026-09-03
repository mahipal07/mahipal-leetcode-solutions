#
# @lc app=leetcode id=3876 lang=python3
#
# [3876] Construct Uniform Parity Array II
#
# 27/27 cases passed (109 ms)
# Your runtime beats 52.11 % of python3 submissions
# Your memory usage beats 28.26 % of python3 submissions (61.4 MB)

# @lc code=start
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return min(nums1) % 2 == 1 or all(x % 2 == 0 for x in nums1)
        
# @lc code=end

