#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# 21/21 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 60.35 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        start_idx = 0
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                start_idx = end_idx
            else:
                start_idx = 0
                
            end_idx = len(res)
            for j in range(start_idx, end_idx):
                res.append(res[j] + [nums[i]])
                
        return res
    
# @lc code=end

