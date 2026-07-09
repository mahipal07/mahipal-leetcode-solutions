#
# @lc app=leetcode id=3532 lang=python3
#
# [3532] Path Existence Queries in a Graph I
#

# @lc code=start
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        comp = [0] * n
        curr = 0
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                curr += 1
            comp[i] = curr
        return [comp[u] == comp[v] for u, v in queries]   
# @lc code=end

