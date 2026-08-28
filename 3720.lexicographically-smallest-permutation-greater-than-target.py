#
# @lc app=leetcode id=3720 lang=python3
#
# [3720] Lexicographically Smallest Permutation Greater Than Target
#
# 761/761 cases passed (58 ms)
# Your runtime beats 5.26 % of python3 submissions
# Your memory usage beats 44.74 % of python3 submissions (19.5 MB)

# @lc code=start
from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_counts = Counter(s)
        prefix_counts = Counter()
        best_k = -1
        best_char = None
        
        for k in range(n):
            remaining = total_counts - prefix_counts
            for ch in sorted(remaining.keys()):
                if ch > target[k] and remaining[ch] > 0:
                    best_k = k
                    best_char = ch
                    break
            
            if remaining[target[k]] > 0:
                prefix_counts[target[k]] += 1
            else:
                break
        
        if best_k == -1:
            return ""
        
        rem_counts = total_counts.copy()
        for ch in target[:best_k]:
            rem_counts[ch] -= 1
        rem_counts[best_char] -= 1
        
        suffix = "".join(sorted(rem_counts.elements()))
        return target[:best_k] + best_char + suffix
        
# @lc code=end

