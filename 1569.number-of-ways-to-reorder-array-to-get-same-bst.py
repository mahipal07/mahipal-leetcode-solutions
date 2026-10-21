#
# @lc app=leetcode id=1569 lang=python3
#
# [1569] Number of Ways to Reorder Array to Get Same BST
#
# 161/161 cases passed (38 ms)
# Your runtime beats 71.89 % of python3 submissions
# Your memory usage beats 36.41 % of python3 submissions (24 MB)

# @lc code=start
import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def count(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            return (
                math.comb(len(left) + len(right), len(left))
                * count(left)
                * count(right)
                % MOD
            )

        return (count(nums) - 1) % MOD
        
# @lc code=end

