#
# @lc app=leetcode id=3534 lang=python3
#
# [3534] Path Existence Queries in a Graph II
#
# 682/682 cases passed (2050 ms)
# Your runtime beats 29.03 % of python3 submissions
# Your memory usage beats 58.06 % of python3 submissions (83.8 MB)

# @lc code=start
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        pairs = sorted((x, i) for i, x in enumerate(nums))
        LOG = 20
        up = [[0] * LOG for _ in range(n)]

        r = n - 1
        for l in range(n - 1, -1, -1):
            while pairs[r][0] - pairs[l][0] > maxDiff:
                r -= 1
            i = pairs[l][1]
            up[i][0] = pairs[r][1]
            for k in range(1, LOG):
                up[i][k] = up[up[i][k - 1]][k - 1]

        ans = []
        for u, v in queries:
            if nums[u] > nums[v]:
                u, v = v, u
            if u == v:
                ans.append(0)
                continue
            if nums[u] == nums[v]:
                ans.append(1)
                continue

            dist = 0
            for k in range(LOG - 1, -1, -1):
                if nums[up[u][k]] < nums[v]:
                    dist |= 1 << k
                    u = up[u][k]

            if nums[up[u][0]] < nums[v]:
                ans.append(-1)
            else:
                ans.append(dist + 1)

        return ans
# @lc code=end

