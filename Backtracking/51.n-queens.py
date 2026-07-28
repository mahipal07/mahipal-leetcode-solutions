#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# 9/9 cases passed (11 ms)
# Your runtime beats 66.24 % of python3 submissions
# Your memory usage beats 9.63 % of python3 submissions (19.9 MB)

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        
        cols = set()
        posDiag = set()
        negDiag = set()

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
        
# @lc code=end

