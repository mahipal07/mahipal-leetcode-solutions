#
# @lc app=leetcode id=3942 lang=python3
#
# [3942] Minimum Operations to Sort a Permutation
#
# 999/999 cases passed (62 ms)
# Your runtime beats 79.55 % of python3 submissions
# Your memory usage beats 86.36 % of python3 submissions (31.4 MB)

# @lc code=start
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        p = nums.index(0)

        is_inc = all(nums[(p + i) % n] == i for i in range(n))
        if is_inc:
            if p == 0:
                return 0
            return min(p, 2 + n - p)

        is_dec = all(nums[(p - i) % n] == i for i in range(n))
        if is_dec:
            return min((p + 1) % n + 1, n - p)

        return -1
    
# @lc code=end

