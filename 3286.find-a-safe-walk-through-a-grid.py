#
# @lc app=leetcode id=3286 lang=python
#
# [3286] Find a Safe Walk Through a Grid
#

# @lc code=start
import collections

class Solution(object):
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])
        dq = collections.deque([(0, 0, health - grid[0][0])])
        visited = {(0, 0): health - grid[0][0]}
        
        while dq:
            r, c, h = dq.popleft()
            
            if h < 1:
                continue
                
            if r == m - 1 and c == n - 1:
                return True
                
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nh = h - grid[nr][nc]
                    if nh > visited.get((nr, nc), -1):
                        visited[(nr, nc)] = nh
                        if grid[nr][nc] == 0:
                            dq.appendleft((nr, nc, nh))
                        else:
                            dq.append((nr, nc, nh))
                            
        return False

# @lc code=end

