#
# @lc app=leetcode id=2685 lang=python3
#
# [2685] Count the Number of Complete Components
#

# @lc code=start
# 3356/3356 cases passed (24 ms)
# Your runtime beats 93.17 % of python3 submissions
# Your memory usage beats 90.53 % of python3 submissions (19.6 MB)

from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        ans = 0
        
        for i in range(n):
            if not visited[i]:
                component = []
                queue = [i]
                visited[i] = True
                
                while queue:
                    curr = queue.pop(0)
                    component.append(curr)
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                v_count = len(component)
                is_complete = True
                for node in component:
                    if len(adj[node]) != v_count - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    ans += 1
                    
        return ans
        
# @lc code=end

