#
# @lc app=leetcode id=1872 lang=python3
#
# [1872] Stone Game VIII
#
# 80/80 cases passed (651 ms)
# Your runtime beats 88.82 % of python3 submissions
# Your memory usage beats 50 % of python3 submissions (33.1 MB)

# @lc code=start
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = list(itertools.accumulate(stones))
        ans = prefix[-1]
        for i in range(n - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)
        return ans
          
# @lc code=end

