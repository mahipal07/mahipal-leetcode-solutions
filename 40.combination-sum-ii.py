#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# 176/176 cases passed (2 ms)
# Your runtime beats 89.62 % of python3 submissions
# Your memory usage beats 13.18 % of python3 submissions (19.6 MB)

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # 1. Sort to handle duplicates and enable pruning
        candidates.sort()

        def backtrack(start, target, path):
            # Base case: we found a valid combination
            if target == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                # 2. Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # 3. Pruning: if the number is greater than the remaining target,
                # no need to check further because the list is sorted.
                if candidates[i] > target:
                    break
                
                # Standard backtracking steps:
                path.append(candidates[i])
                # i + 1 because we can't reuse the same element
                backtrack(i + 1, target - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return res
     
# @lc code=end

