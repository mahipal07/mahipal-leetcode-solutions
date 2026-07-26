#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# 128/128 cases passed (9 ms)
# Your runtime beats 89.48 % of python3 submissions
# Your memory usage beats 16.66 % of python3 submissions (24 MB)

# @lc code=start
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
      
# @lc code=end

