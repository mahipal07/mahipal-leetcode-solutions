#
# @lc app=leetcode id=1189 lang=python
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text):
        from collections import Counter
        freq = Counter(text)
        
        return min(
            freq['b'],
            freq['a'],
            freq['l'] // 2,
            freq['o'] // 2,
            freq['n']
        )

        
# @lc code=end

