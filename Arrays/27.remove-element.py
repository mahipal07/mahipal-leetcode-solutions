#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
# 116/116 cases passed (1 ms)
# Your runtime beats 5.4 % of python3 submissions
# Your memory usage beats 18.69 % of python3 submissions (19.3 MB)

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
        
# @lc code=end

