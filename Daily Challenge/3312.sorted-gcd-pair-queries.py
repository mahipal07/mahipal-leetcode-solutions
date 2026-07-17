#
# @lc app=leetcode id=3312 lang=python3
#
# [3312] Sorted GCD Pair Queries
#
# 721/721 cases passed (718 ms)
# Your runtime beats 25 % of python3 submissions
# Your memory usage beats 22.5 % of python3 submissions (41.4 MB)

# @lc code=start
from typing import List
from collections import Counter
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        counts = Counter(nums)
        
        gcd_cnt = [0] * (max_val + 1)
        
        for i in range(max_val, 0, -1):
            divisible_count = 0
            for j in range(i, max_val + 1, i):
                divisible_count += counts[j]
            
            pairs = (divisible_count * (divisible_count - 1)) // 2
            
            for j in range(2 * i, max_val + 1, i):
                pairs -= gcd_cnt[j]
                
            gcd_cnt[i] = pairs
            
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + gcd_cnt[i]
            
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans
    
# @lc code=end

