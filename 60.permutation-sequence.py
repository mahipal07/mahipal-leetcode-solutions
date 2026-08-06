#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
# 200/200 cases passed (2 ms)
# Your runtime beats 31.24 % of python3 submissions
# Your memory usage beats 88.5 % of python3 submissions (19.3 MB)

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1
        result = []
        
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            result.append(numbers.pop(index))
            k %= fact
            
        return "".join(result)
        
# @lc code=end

