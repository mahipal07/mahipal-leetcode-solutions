#
# @lc app=leetcode id=2267 lang=python3
#
# [2267]  Check if There Is a Valid Parentheses String Path
#
# 81/81 cases passed (1416 ms)
# Your runtime beats 14 % of python3 submissions
# Your memory usage beats 36 % of python3 submissions (54.9 MB)

# @lc code=start
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 != 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        visited = set()
        queue = {(0, 0, 1)}

        while queue:
            next_queue = set()
            for r, c, bal in queue:
                if r == m - 1 and c == n - 1:
                    if bal == 0:
                        return True
                    continue

                for dr, dc in ((0, 1), (1, 0)):
                    nr, nc = r + dr, c + dc
                    if nr < m and nc < n:
                        n_bal = bal + (1 if grid[nr][nc] == '(' else -1)
                        if n_bal >= 0 and n_bal <= (m - 1 - nr) + (n - 1 - nc):
                            state = (nr, nc, n_bal)
                            if state not in visited:
                                visited.add(state)
                                next_queue.add(state)
                                
            queue = next_queue

        return False
     
# @lc code=end

