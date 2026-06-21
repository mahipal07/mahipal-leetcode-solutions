#
# @lc app=leetcode id=1833 lang=python
#
# [1833] Maximum Ice Cream Bars
#

# @lc code=start
class Solution(object):
    def maxIceCream(self, costs, coins):
        # Sort costs so cheapest comes first
        costs.sort()
        
        count = 0
        for price in costs:
            if coins >= price:
                coins -= price
                count += 1
            else:
                break
        return count

        
# @lc code=end

