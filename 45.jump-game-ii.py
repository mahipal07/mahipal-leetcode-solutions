#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# 111/111 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 65.65 % of python3 submissions (20 MB)

# @lc code=start
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                if current_end >= n - 1:
                    break
                    
        return jumps
        
# @lc code=end

