#
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#
# 24/24 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 64.31 % of python3 submissions (19.3 MB)

# @lc code=start
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        digits = "123456789"
        
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(10 - length):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    result.append(num)
                    
        return result
        
# @lc code=end

