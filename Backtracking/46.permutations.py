#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# 26/26 cases passed (1 ms)
# Your runtime beats 45.2 % of python3 submissions
# Your memory usage beats 33.26 % of python3 submissions (19.6 MB)

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return res
    
# @lc code=end

