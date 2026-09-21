#
# @lc app=leetcode id=3524 lang=python3
#
# [3524] Find X Value of Array I
#
# 782/782 cases passed (334 ms)
# Your runtime beats 81.58 % of python3 submissions
# Your memory usage beats 85.53 % of python3 submissions (34 MB)

# @lc code=start
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
        
        for num in nums:
            val = num % k
            next_dp = [0] * k
            next_dp[val] += 1
            
            for rem in range(k):
                if dp[rem]:
                    next_dp[(rem * val) % k] += dp[rem]
            
            dp = next_dp
            for rem in range(k):
                ans[rem] += dp[rem]
                
        return ans
    
# @lc code=end

