#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# 178/178 cases passed (4 ms)
# Your runtime beats 99.44 % of python3 submissions
# Your memory usage beats 29.43 % of python3 submissions (20.5 MB)

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            if n > gas:
                gas = n
            gas -= 1
        return True
        
# @lc code=end

