#
# @lc app=leetcode id=2213 lang=python3
#
# [2213] Longest Substring of One Repeating Character
#
# 57/57 cases passed (4591 ms)
# Your runtime beats 8.2 % of python3 submissions
# Your memory usage beats 14.76 % of python3 submissions (115.1 MB)

# @lc code=start
class Node:
    def __init__(self, maxLen=0, prefLen=0, suffLen=0,
                 leftChar='', rightChar='', length=0):
        self.maxLen = maxLen
        self.prefLen = prefLen
        self.suffLen = suffLen
        self.leftChar = leftChar
        self.rightChar = rightChar
        self.len = length


class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        tree = [None] * (4 * n)

        def merge(L, R):
            res = Node()
            res.len = L.len + R.len
            res.leftChar = L.leftChar
            res.rightChar = R.rightChar

            # Prefix
            res.prefLen = L.prefLen
            if L.prefLen == L.len and L.rightChar == R.leftChar:
                res.prefLen += R.prefLen

            # Suffix
            res.suffLen = R.suffLen
            if R.suffLen == R.len and L.rightChar == R.leftChar:
                res.suffLen += L.suffLen

            # Maximum
            cross = 0
            if L.rightChar == R.leftChar:
                cross = L.suffLen + R.prefLen

            res.maxLen = max(L.maxLen, R.maxLen, cross)

            return res

        def build(node, start, end):
            if start == end:
                tree[node] = Node(
                    1, 1, 1,
                    s[start], s[start], 1
                )
                return

            mid = start + (end - start) // 2

            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)

            tree[node] = merge(
                tree[2 * node],
                tree[2 * node + 1]
            )

        def update(node, start, end, idx, ch):
            if start == end:
                tree[node] = Node(
                    1, 1, 1,
                    ch, ch, 1
                )
                return

            mid = start + (end - start) // 2

            if idx <= mid:
                update(2 * node, start, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, end, idx, ch)

            tree[node] = merge(
                tree[2 * node],
                tree[2 * node + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for i in range(len(queryIndices)):
            update(
                1,
                0,
                n - 1,
                queryIndices[i],
                queryCharacters[i]
            )
            ans.append(tree[1].maxLen)

        return ans
         
# @lc code=end

