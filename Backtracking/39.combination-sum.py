#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# 160/160 cases passed (15 ms)
# Your runtime beats 21.89 % of python3 submissions
# Your memory usage beats 32.22 % of python3 submissions (19.6 MB)

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, cur, total):
            # Base Case: Found a valid combination
            if total == target:
                res.append(cur.copy())
                return
            
            # Base Case: Out of bounds or sum exceeded target
            if i >= len(candidates) or total > target:
                return

            # Choice 1: Include candidates[i]
            cur.append(candidates[i])
            backtrack(i, cur, total + candidates[i])
            
            # Choice 2: Skip candidates[i] (Backtrack)
            cur.pop()
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)
        return res
    
# @lc code=end

