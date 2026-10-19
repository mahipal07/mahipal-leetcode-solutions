#
# @lc app=leetcode id=2913 lang=python3
#
# [2913] Subarrays Distinct Element Sum of Squares I
#
# 707/707 cases passed (18 ms)
# Your runtime beats 87.34 % of python3 submissions
# Your memory usage beats 8.46 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for i in range(n):
            distinct = set()
            for j in range(i, n):
                distinct.add(nums[j])
                total += len(distinct) ** 2
        return total
    
# @lc code=end

