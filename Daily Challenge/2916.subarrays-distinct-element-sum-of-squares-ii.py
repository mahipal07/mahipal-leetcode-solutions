#
# @lc app=leetcode id=2916 lang=python3
#
# [2916] Subarrays Distinct Element Sum of Squares II
#

# 542/542 cases passed (5159 ms)
# Your runtime beats 19.85 % of python3 submissions
# Your memory usage beats 12.46 % of python3 submissions (123.9 MB)

# @lc code=start
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        
        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push_up(node):
            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD
            tree_sq[node] = (tree_sq[2 * node] + tree_sq[2 * node + 1]) % MOD

        def apply(node, l, r, val):
            length = r - l + 1
            tree_sq[node] = (tree_sq[node] + 2 * val * tree_sum[node] + val * val * length) % MOD
            tree_sum[node] = (tree_sum[node] + val * length) % MOD
            lazy[node] = (lazy[node] + val) % MOD

        def push_down(node, l, r):
            if lazy[node]:
                mid = (l + r) // 2
                apply(2 * node, l, mid, lazy[node])
                apply(2 * node + 1, mid + 1, r, lazy[node])
                lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                apply(node, l, r, val)
                return
            push_down(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(2 * node, l, mid, ql, qr, val)
            if qr > mid:
                update(2 * node + 1, mid + 1, r, ql, qr, val)
            push_up(node)

        last_pos = {}
        ans = 0
        
        for i, x in enumerate(nums):
            prev = last_pos.get(x, -1)
            update(1, 0, n - 1, prev + 1, i, 1)
            ans = (ans + tree_sq[1]) % MOD
            last_pos[x] = i
            
        return ans
        
# @lc code=end

