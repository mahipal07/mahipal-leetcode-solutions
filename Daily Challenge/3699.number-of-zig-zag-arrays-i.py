#
# @lc app=leetcode id=3699 lang=python
#
# [3699] Number of ZigZag Arrays I
#

# @lc code=start
MOD = 10**9 + 7

class Solution(object):
    def zigZagArrays(self, n, l, r):
        m = r - l + 1
        # dp_up[x] = ways ending at x with last move up
        # dp_down[x] = ways ending at x with last move down
        dp_up = [1] * (m+1)
        dp_down = [1] * (m+1)
        
        for i in range(2, n+1):
            prefix_up = [0] * (m+2)
            prefix_down = [0] * (m+2)
            
            for x in range(1, m+1):
                prefix_up[x] = (prefix_up[x-1] + dp_up[x]) % MOD
            for x in range(m, 0, -1):
                prefix_down[x] = (prefix_down[x+1] + dp_down[x]) % MOD
            
            new_up = [0] * (m+1)
            new_down = [0] * (m+1)
            
            for y in range(1, m+1):
                new_down[y] = prefix_up[y-1]      # must go down
                new_up[y] = prefix_down[y+1]      # must go up
            
            dp_up, dp_down = new_up, new_down
        
        ans = 0
        for x in range(1, m+1):
            ans = (ans + dp_up[x] + dp_down[x]) % MOD
        return ans


        
# @lc code=end

