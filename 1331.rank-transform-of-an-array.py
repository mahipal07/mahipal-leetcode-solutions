#
# @lc app=leetcode id=1331 lang=python3
#
# [1331] Rank Transform of an Array
#
# 43/43 cases passed (35 ms)
# Your runtime beats 76.35 % of python3 submissions
# Your memory usage beats 60.61 % of python3 submissions (37.5 MB)

# @lc code=start
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {val: i + 1 for i, val in enumerate(sorted(set(arr)))}
        return [ranks[x] for x in arr]
        
# @lc code=end

