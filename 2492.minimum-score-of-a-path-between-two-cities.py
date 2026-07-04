#
# @lc app=leetcode id=2492 lang=python3
#
# [2492] Minimum Score of a Path Between Two Cities
#

# @lc code=start
from collections import deque, defaultdict
import sys

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        graph = defaultdict(list)
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))
        
        min_score = sys.maxsize
        visited = {1}
        queue = deque([1])
        
        while queue:
            node = queue.popleft()
            for neighbor, distance in graph[node]:
                min_score = min(min_score, distance)
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score
        
# @lc code=end

