#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
# 8/8 cases passed (1188 ms)
# Your runtime beats 63.45 % of python3 submissions
# Your memory usage beats 58.3 % of python3 submissions (19.6 MB)

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        # Sets to track used numbers in rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Pre-fill sets and find all empty spots
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)
                else:
                    empty_cells.append((r, c))

        def backtrack(index):
            if index == len(empty_cells):
                return True
            
            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + (c // 3)
            
            for num in "123456789":
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_idx]:
                    # Place number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)
                    
                    if backtrack(index + 1):
                        return True
                    
                    # Backtrack (Remove number)
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)
            
            return False

        backtrack(0)
        
# @lc code=end

