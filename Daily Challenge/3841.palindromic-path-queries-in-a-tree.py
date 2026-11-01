#
# @lc app=leetcode id=3841 lang=python3
#
# [3841] Palindromic Path Queries in a Tree
#
# 1040/1040 cases passed (1418 ms)
# Your runtime beats 59.13 % of python3 submissions
# Your memory usage beats 54.37 % of python3 submissions (64.4 MB)

# @lc code=start
import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(300000)

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        LOGN = (n).bit_length() + 1
        up = [[0] * LOGN for _ in range(n)]
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        initial_P = [0] * n
        timer = 0
        
        # Keep track of current characters as bitmasks
        chars = [1 << (ord(c) - 97) for c in s]
        
        # Iterative DFS to avoid potential recursion limit issues
        parent = [-1] * n
        order = []
        stack = [0]
        visited = [False] * n
        visited[0] = True
        
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)
                    
        # Compute DFS entry/exit times, initial P(u), and binary lifting table
        # We can run a quick recursive or stack-based tour for entry/exit times
        tin_tout_stack = [(0, 0, False)]  # (node, parent, processed)
        timer = 1
        
        # Re-run proper DFS order for tin/tout
        tin = [0] * n
        tout = [0] * n
        
        call_stack = [(0, 0)]
        adj_idx = [0] * n
        initial_P[0] = chars[0]
        tin[0] = 1
        timer = 2
        
        while call_stack:
            u, p = call_stack[-1]
            up[u][0] = p
            
            advanced = False
            while adj_idx[u] < len(adj[u]):
                v = adj[u][adj_idx[u]]
                adj_idx[u] += 1
                if v != p:
                    initial_P[v] = initial_P[u] ^ chars[v]
                    tin[v] = timer
                    timer += 1
                    call_stack.append((v, u))
                    advanced = True
                    break
                    
            if not advanced:
                tout[u] = timer - 1
                call_stack.pop()
                
        # Fill binary lifting table
        for j in range(1, LOGN):
            for i in range(n):
                up[i][j] = up[up[i][j - 1]][j - 1]
                
        def is_ancestor(u, v):
            return tin[u] <= tin[v] and tout[u] >= tout[v]
            
        def lca(u, v):
            if is_ancestor(u, v):
                return u
            if is_ancestor(v, u):
                return v
            for j in range(LOGN - 1, -1, -1):
                if not is_ancestor(up[u][j], v):
                    u = up[u][j]
            return up[u][0]

        # Fenwick Tree for Range Updates & Point Queries (XOR)
        bit = [0] * (n + 2)
        
        def bit_update(idx, val):
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def bit_query(idx):
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res
            
        def get_P(u):
            # initial_P XOR accumulated subtree updates
            return initial_P[u] ^ bit_query(tin[u])
            
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_char_mask = 1 << (ord(parts[2]) - 97)
                diff = chars[u] ^ new_char_mask
                chars[u] = new_char_mask
                
                # Apply range XOR update on subtree [tin[u], tout[u]]
                bit_update(tin[u], diff)
                bit_update(tout[u] + 1, diff)
            else:
                u = int(parts[1])
                v = int(parts[2])
                w = lca(u, v)
                
                # Path XOR sum
                path_mask = get_P(u) ^ get_P(v) ^ chars[w]
                
                # Palindrome check: at most one bit set
                can_form = (path_mask & (path_mask - 1)) == 0
                ans.append(can_form)
                
        return ans
    
# @lc code=end

