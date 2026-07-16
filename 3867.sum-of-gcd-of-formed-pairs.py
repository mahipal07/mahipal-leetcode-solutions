#
# @lc app=leetcode id=3867 lang=python3
#
# [3867] Sum of GCD of Formed Pairs
# 
# 1012/1012 cases passed (197 ms)
# Your runtime beats 61.68 % of python3 submissions
# Your memory usage beats 91.62 % of python3 submissions (33.3 MB)

# @lc code=start
import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = [0] * n
        
        current_max = 0
        for i in range(n):
            if nums[i] > current_max:
                current_max = nums[i]
            prefixGcd[i] = math.gcd(nums[i], current_max)
            
        prefixGcd.sort()
        
        total_sum = 0
        left = 0
        right = n - 1
        
        while left < right:
            total_sum += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_sum
        
# @lc code=end

