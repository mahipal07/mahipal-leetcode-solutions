#
# @lc app=leetcode id=1477 lang=python3
#
# [1477] Find Two Non-overlapping Sub-arrays Each With Target Sum
#
# 61/61 cases passed (176 ms)
# Your runtime beats 47.48 % of python3 submissions
# Your memory usage beats 34.64 % of python3 submissions (42.3 MB)

# @lc code=start
class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        prefix_sum = 0
        sum_idx = {0: -1}
        n = len(arr)
        min_len_so_far = [float('inf')] * n
        
        min_sum = float('inf')
        current_min_len = float('inf')
        
        for i, val in enumerate(arr):
            prefix_sum += val
            sum_idx[prefix_sum] = i
            
            needed = prefix_sum - target
            if needed in sum_idx:
                start_idx = sum_idx[needed]
                length = i - start_idx
                current_min_len = min(current_min_len, length)
                
                if start_idx >= 0 and min_len_so_far[start_idx] != float('inf'):
                    min_sum = min(min_sum, length + min_len_so_far[start_idx])
            
            min_len_so_far[i] = current_min_len
            
        return min_sum if min_sum != float('inf') else -1 
# @lc code=end

