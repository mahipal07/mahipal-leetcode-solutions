#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
# 507/507 cases passed (3 ms)
# Your runtime beats 75.16 % of python3 submissions
# Your memory usage beats 34.4 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use collections.defaultdict(set) to store seen numbers
        import collections
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # Check if value already exists in current row, column, or square
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[(r // 3, c // 3)]):
                    return False
                
                # Add value to the respective sets
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)
                
        return True
        
# @lc code=end

