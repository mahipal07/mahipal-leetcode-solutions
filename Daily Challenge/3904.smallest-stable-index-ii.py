#
# @lc app=leetcode id=3904 lang=python3
#
# [3904] Smallest Stable Index II
#
# Accepted
# 928/928 cases passed (140 ms)
# Your runtime beats 83.64 % of python3 submissions
# Your memory usage beats 7.27 % of python3 submissions (33.5 MB)

# @lc code=start
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        
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

