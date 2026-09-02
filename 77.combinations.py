#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# 27/27 cases passed (109 ms)
# Your runtime beats 52.11 % of python3 submissions
# Your memory usage beats 28.26 % of python3 submissions (61.4 MB)

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(start: int, current_comb: List[int]):
            # If the combination is done
            if len(current_comb) == k:
                res.append(list(current_comb))
                return
            
            # Optimization: There's no need to iterate if there aren't 
            # enough elements left to make a combination of size k
            # Elements needed = k - len(current_comb)
            # Elements available = n - start + 1
            for i in range(start, n + 1):
                # Add the current element
                current_comb.append(i)
                # Move onto the next element
                backtrack(i + 1, current_comb)
                # Backtrack: remove the element before trying the next one
                current_comb.pop()
                
        backtrack(1, [])
        return res
        
# @lc code=end

