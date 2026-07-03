#
# @lc app=leetcode id=1358 lang=python
#
# [1358] Number of Substrings Containing All Three Characters
#
# 54/54 cases passed (87 ms)
# Your runtime beats 95.77 % of python submissions
# Your memory usage beats 84.99 % of python submissions (12.6 MB)

# @lc code=start
class Solution(object):
    def numberOfSubstrings(self, s):
        res = 0
        last = {'a': -1, 'b': -1, 'c': -1}
        for i, ch in enumerate(s):
            last[ch] = i
            res += min(last['a'], last['b'], last['c']) + 1
        return res

# @lc code=end

