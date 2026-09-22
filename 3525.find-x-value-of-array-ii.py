#
# @lc app=leetcode id=3525 lang=python3
#
# [3525] Find X Value of Array II
#
# 783/783 cases passed (3948 ms)
# Your runtime beats 94.12 % of python3 submissions
# Your memory usage beats 58.82 % of python3 submissions (66.2 MB)

# @lc code=start
class SegmentTree:
    def __init__(self, data, k):
        self.n = len(data)
        self.k = k
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.tree_prod = [1] * (2 * self.size)
        self.tree_cnt = [[0] * k for _ in range(2 * self.size)]
        
        for i in range(self.n):
            idx = self.size + i
            val = data[i] % k
            self.tree_prod[idx] = val
            self.tree_cnt[idx][val] = 1
            
        for i in range(self.size - 1, 0, -1):
            self._pull(i)

    def _pull(self, idx):
        left = 2 * idx
        right = 2 * idx + 1
        self.tree_prod[idx] = (self.tree_prod[left] * self.tree_prod[right]) % self.k
        cnt = list(self.tree_cnt[left])
        prod_left = self.tree_prod[left]
        for rem in range(self.k):
            c = self.tree_cnt[right][rem]
            if c:
                cnt[(prod_left * rem) % self.k] += c
        self.tree_cnt[idx] = cnt

    def update(self, pos, val):
        idx = self.size + pos
        val %= self.k
        self.tree_prod[idx] = val
        self.tree_cnt[idx] = [0] * self.k
        self.tree_cnt[idx][val] = 1
        idx >>= 1
        while idx > 0:
            self._pull(idx)
            idx >>= 1

    def query(self, l, r, target):
        l += self.size
        r += self.size
        left_nodes = []
        right_nodes = []
        while l <= r:
            if l % 2 == 1:
                left_nodes.append(l)
                l += 1
            if r % 2 == 0:
                right_nodes.append(r)
                r -= 1
            l >>= 1
            r >>= 1
            
        nodes = left_nodes + right_nodes[::-1]
        
        ans = 0
        cur_prod = 1
        for node in nodes:
            for rem in range(self.k):
                c = self.tree_cnt[node][rem]
                if c and (cur_prod * rem) % self.k == target:
                    ans += c
            cur_prod = (cur_prod * self.tree_prod[node]) % self.k
            
        return ans

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        st = SegmentTree(nums, k)
        res = []
        for idx, val, start, x in queries:
            st.update(idx, val)
            res.append(st.query(start, n - 1, x))
        return res
    
# @lc code=end

