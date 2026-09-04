#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# 88/88 cases passed (3426 ms)
# Your runtime beats 70.75 % of python3 submissions
# Your memory usage beats 28.71 % of python3 submissions (19.5 MB)

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                board[r][c] != word[i]):
                return False
            
            temp = board[r][c]
            board[r][c] = "#"
            
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            board[r][c] = temp
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
    
# @lc code=end

