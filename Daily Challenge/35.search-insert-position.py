#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# Accepted
# 66/66 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 11.19 % of python3 submissions (20 MB)

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
# @lc code=end

