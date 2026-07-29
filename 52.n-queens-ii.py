#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
# 9/9 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 83.86 % of python3 submissions (19.2 MB)

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        # done is a bitmask with n ones (e.g., if n=4, done = 1111 in binary)
        done = (1 << n) - 1

        def backtrack(cols, pos_diag, neg_diag):
            if cols == done:
                self.count += 1
                return

            # Find all available positions in the current row
            # (cols | pos_diag | neg_diag) gives all attacked positions
            # ~ negates it, and & done keeps it within the n-bit range
            possibilities = ~(cols | pos_diag | neg_diag) & done

            while possibilities:
                # Extract the rightmost set bit (the position to place a queen)
                bit = possibilities & -possibilities
                # Remove that bit from possibilities
                possibilities -= bit
                
                # Move to the next row:
                # - cols | bit: mark column as occupied
                # - (pos_diag | bit) << 1: shift diagonal for next row
                # - (neg_diag | bit) >> 1: shift anti-diagonal for next row
                backtrack(cols | bit, (pos_diag | bit) << 1, (neg_diag | bit) >> 1)

        backtrack(0, 0, 0)
        return self.count
    
# @lc code=end

