#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# 33/33 cases passed (7 ms)
# Your runtime beats 42.75 % of python3 submissions
# Your memory usage beats 54.16 % of python3 submissions (19.9 MB)

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def backtrack(current, options):
            if not options:
                res.append(current)
                return
            
            for i in range(len(options)):
                if i > 0 and options[i] == options[i-1]:
                    continue
                backtrack(current + [options[i]], options[:i] + options[i+1:])
        
        backtrack([], nums)
        return res
        
# @lc code=end

