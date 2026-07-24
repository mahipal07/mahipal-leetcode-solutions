#
# @lc app=leetcode id=3514 lang=python3
#
# [3514] Number of Unique XOR Triplets II
#
# 825/825 cases passed (4815 ms)
# Your runtime beats 66.67 % of python3 submissions
# Your memory usage beats 62.96 % of python3 submissions (19.5 MB)

# @lc code=start
class Solution:

    def uniqueXorTriplets(self, nums: List[int]) -> int:
        U = list(set(nums))
        S2 = {a ^ b for a in U for b in U}
        return len({x ^ c for x in S2 for c in U})
    
# @lc code=end

