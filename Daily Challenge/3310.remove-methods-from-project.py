#
# @lc app=leetcode id=3310 lang=python3
#
# [3310] Remove Methods From Project
#
# 775/775 cases passed (217 ms)
# Your runtime beats 93.94 % of python3 submissions
# Your memory usage beats 96.97 % of python3 submissions (99.5 MB)

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]

        for u, v in invocations:
            adj[u].append(v)

        suspicious = [False] * n
        q = deque([k])
        suspicious[k] = True

        # BFS to mark all suspicious methods
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    q.append(v)

        # Check if any non-suspicious method invokes a suspicious one
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Return all non-suspicious methods
        remaining = []
        for i in range(n):
            if not suspicious[i]:
                remaining.append(i)

        return remaining
       
# @lc code=end

