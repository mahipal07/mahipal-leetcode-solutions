#
# @lc app=leetcode id=835 lang=python3
#
# [835] Image Overlap
#
# 60/60 cases passed (163 ms)
# Your runtime beats 94.44 % of python3 submissions
# Your memory usage beats 6.35 % of python3 submissions (20.1 MB)

# @lc code=start
from collections import Counter
from typing import List


class Solution:

  def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
    n = len(img1)

    ones1 = [
        (r, c) for r in range(n) for c in range(n) if img1[r][c] == 1
    ]
    ones2 = [
        (r, c) for r in range(n) for c in range(n) if img2[r][c] == 1
    ]

    shift_counts = Counter(
        (r2 - r1, c2 - c1) for r1, c1 in ones1 for r2, c2 in ones2
    )

    return max(shift_counts.values(), default=0)
    
# @lc code=end

