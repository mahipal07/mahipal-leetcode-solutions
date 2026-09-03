#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# 10/10 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 28.42 % of python3 submissions (19.5 MB)

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(index, path):
            res.append(list(path))
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(0, [])
        return res
        
# @lc code=end

