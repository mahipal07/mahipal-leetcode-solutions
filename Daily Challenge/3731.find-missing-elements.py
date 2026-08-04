#
# @lc app=leetcode id=3731 lang=python3
#
# [3731] Find Missing Elements
#
# 989/989 cases passed (3 ms)
# Your runtime beats 69.59 % of python3 submissions
# Your memory usage beats 86.89 % of python3 submissions (19.2 MB)

# @lc code=start
class Solution:
    def findMissingElements(self, nums):
        min_val = min(nums)
        max_val = max(nums)
        present = set(nums)

        result = []
        for i in range(min_val, max_val + 1):
            if i not in present:
                result.append(i)

        return result
    
# @lc code=end

