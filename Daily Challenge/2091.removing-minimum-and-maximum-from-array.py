#
# @lc app=leetcode id=2091 lang=python3
#
# [2091] Removing Minimum and Maximum From Array
#
# 62/62 cases passed (27 ms)
# Your runtime beats 31.12 % of python3 submissions
# Your memory usage beats 80.97 % of python3 submissions (33.4 MB)

# @lc code=start
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        i, j = min(min_idx, max_idx), max(min_idx, max_idx)

        option1 = j + 1
        option2 = n - i
        option3 = (i + 1) + (n - j)

        return min(option1, option2, option3)
        
# @lc code=end

