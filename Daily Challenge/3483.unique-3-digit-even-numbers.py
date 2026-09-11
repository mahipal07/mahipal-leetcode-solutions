#
# @lc app=leetcode id=3483 lang=python3
#
# [3483] Unique 3-Digit Even Numbers
#

# @lc code=start
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        from collections import Counter

        count = Counter(digits)
        ans = 0

        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            req = Counter((d1, d2, d3))
            if all(count[d] >= req[d] for d in req):
                ans += 1

        return ans
    
# @lc code=end

