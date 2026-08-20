#
# @lc app=leetcode id=3069 lang=python3
#
# [3069] Distribute Elements Into Two Arrays I
#
# 622/622 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 22.76 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        
        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
                
        return arr1 + arr2
        
# @lc code=end

