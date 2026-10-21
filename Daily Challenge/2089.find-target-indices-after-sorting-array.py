#
# @lc app=leetcode id=2089 lang=python3
#
# [2089] Find Target Indices After Sorting Array
#
# 216/216 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 72.69 % of python3 submissions (19.1 MB)

# @lc code=start
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less = sum(1 for x in nums if x < target)
        count = sum(1 for x in nums if x == target)
        return list(range(less, less + count))
    
# @lc code=end

