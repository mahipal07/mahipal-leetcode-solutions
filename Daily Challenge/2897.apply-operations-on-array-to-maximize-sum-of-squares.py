#
# @lc app=leetcode id=2897 lang=python3
#
# [2897] Apply Operations on Array to Maximize Sum of Squares
#
# 918/918 cases passed (1395 ms)
# Your runtime beats 69.63 % of python3 submissions
# Your memory usage beats 49.65 % of python3 submissions (32.1 MB)

# @lc code=start
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 31
        
        for num in nums:
            for b in range(31):
                if (num >> b) & 1:
                    bit_counts[b] += 1
                    
        total = 0
        for _ in range(k):
            val = 0
            for b in range(31):
                if bit_counts[b] > 0:
                    val |= (1 << b)
                    bit_counts[b] -= 1
            total = (total + val * val) % MOD
            
        return total
        
# @lc code=end

