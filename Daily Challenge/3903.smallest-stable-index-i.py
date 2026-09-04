#
# @lc app=leetcode id=3903 lang=python3
#
# [3903] Smallest Stable Index I
#
# 941/941 cases passed (2 ms)
# Your runtime beats 81.53 % of python3 submissions
# Your memory usage beats 71.43 % of python3 submissions (19.3 MB)

# @lc code=start
class Solution:

    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        min_suffix = [0] * n
        min_suffix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(nums[i], min_suffix[i + 1])

        max_prefix = nums[0]
        for i in range(n):
            max_prefix = max(max_prefix, nums[i])
            if max_prefix - min_suffix[i] <= k:
                return i

        return -1
        
# @lc code=end

