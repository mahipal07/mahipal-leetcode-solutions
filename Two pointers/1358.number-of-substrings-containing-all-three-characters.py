#
# @lc app=leetcode id=1358 lang=python
#
# [1358] Number of Substrings Containing All Three Characters
#

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

