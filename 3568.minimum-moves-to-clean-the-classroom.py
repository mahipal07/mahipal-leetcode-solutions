#
# @lc app=leetcode id=3568 lang=python3
#
# [3568] Minimum Moves to Clean the Classroom
#
# 799/799 cases passed (2144 ms)
# Your runtime beats 63.16 % of python3 submissions
# Your memory usage beats 64.91 % of python3 submissions (60 MB)

# @lc code=start
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        start = None
        litters = []
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litters.append((r, c))
                    
        num_litters = len(litters)
        if num_litters == 0:
            return 0
            
        litter_idx = {pos: i for i, pos in enumerate(litters)}
        all_litters_mask = (1 << num_litters) - 1
        
        # BFS state: (row, col, collected_mask, current_energy)
        # Visited tracking: visited[r][c][mask] = max_energy_seen
        visited = {}
        
        queue = deque([(start[0], start[1], 0, energy, 0)])
        visited[(start[0], start[1], 0)] = energy
        
        while queue:
            r, c, mask, cur_energy, moves = queue.popleft()
            
            if mask == all_litters_mask:
                return moves
                
            if cur_energy == 0:
                continue
                
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_energy = cur_energy - 1
                    cell_type = classroom[nr][nc]
                    
                    if cell_type == 'R':
                        next_energy = energy
                        
                    next_mask = mask
                    if cell_type == 'L' and (nr, nc) in litter_idx:
                        idx = litter_idx[(nr, nc)]
                        next_mask |= (1 << idx)
                        
                    state_key = (nr, nc, next_mask)
                    if visited.get(state_key, -1) < next_energy:
                        visited[state_key] = next_energy
                        queue.append((nr, nc, next_mask, next_energy, moves + 1))
                        
        return -1
    
# @lc code=end

