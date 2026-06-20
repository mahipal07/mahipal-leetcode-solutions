#
# @lc app=leetcode id=1840 lang=python3
#
# [1840] Maximum Building Height
#

# @lc code=start
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()
        
        m = len(restrictions)
        
        for i in range(1, m):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + (restrictions[i][0] - restrictions[i-1][0]))
            
        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + (restrictions[i+1][0] - restrictions[i][0]))
            
        max_height = 0
        for i in range(m - 1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i+1]
            max_height = max(max_height, (h1 + h2 + id2 - id1) // 2)
            
        max_height = max(max_height, restrictions[-1][1] + (n - restrictions[-1][0]))
        
        return max_height


# @lc code=end

