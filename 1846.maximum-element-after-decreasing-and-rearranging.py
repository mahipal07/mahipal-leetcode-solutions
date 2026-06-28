#
# @lc app=leetcode id=1846 lang=python
#
# [1846] Maximum Element After Decreasing and Rearranging
#

# @lc code=start
class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        ans = 1
        for x in arr[1:]:
            ans = min(x, ans + 1)
        return ans
# @lc code=end

