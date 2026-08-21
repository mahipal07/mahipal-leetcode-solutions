#
# @lc app=leetcode id=3116 lang=python3
#
# [3116] Kth Smallest Amount With Single Denomination Combination
#
# 561/561 cases passed (1473 ms)
# Your runtime beats 10.98 % of python3 submissions
# Your memory usage beats 93.9 % of python3 submissions (19.3 MB)

# @lc code=start
from math import lcm
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        def count(m: int) -> int:
            total = 0
            for mask in range(1, 1 << n):
                cur_lcm = 1
                bits = 0
                for i in range(n):
                    if (mask >> i) & 1:
                        bits += 1
                        cur_lcm = lcm(cur_lcm, coins[i])
                
                if bits % 2 == 1:
                    total += m // cur_lcm
                else:
                    total -= m // cur_lcm
            return total

        low = 1
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
       
# @lc code=end

