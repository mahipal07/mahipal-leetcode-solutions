#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum

#Accepted
# 294/294 cases passed (539 ms)
# Your runtime beats 38 % of python submissions
# Your memory usage beats 63.76 % of python submissions (12.3 MB)

# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        n = len(nums)
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
                        
        return results


        
# @lc code=end

