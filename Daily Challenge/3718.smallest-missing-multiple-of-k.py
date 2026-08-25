#
# @lc app=leetcode id=3718 lang=python3
#
# [3718] Smallest Missing Multiple of K
#
# 664/664 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 53.35 % of python3 submissions (19.3 MB)

# @lc code=start
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        curr = k
        while curr in num_set:
            curr += k
        return curr
        
# @lc code=end

