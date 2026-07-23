#
# @lc app=leetcode id=3513 lang=python3
#
# [3513] Number of Unique XOR Triplets I

#785/785 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 76.27 % of python3 submissions (31.9 MB)

# @lc code=start
class Solution:

    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        if n == 2:
            return 2
        return 1 << n.bit_length()
    
# @lc code=end

