#
# @lc app=leetcode id=3260 lang=python
#
# [3260] Find the Largest Palindrome Divisible by K
#
# 632/632 cases passed (0 ms)
# Your runtime beats 100 % of python submissions [WARN] Failed to get memory percentile.

# @lc code=start
class Solution(object):
    def largestPalindrome(self, n, k):
        if k == 1:
            return '9' * n
        if k == 2:
            return '8' * n if n <= 2 else '8' + '9' * (n - 2) + '8'
        if k == 3 or k == 9:
            return '9' * n
        if k == 4:
            return '8' * n if n <= 4 else '88' + '9' * (n - 4) + '88'
        if k == 5:
            return '5' * n if n <= 2 else '5' + '9' * (n - 2) + '5'
        if k == 6:
            if n <= 2:
                return '6' * n
            if n % 2:
                l = n // 2 - 1
                return '8' + '9' * l + '8' + '9' * l + '8'
            l = n // 2 - 2
            return '8' + '9' * l + '77' + '9' * l + '8'
        if k == 8:
            return '8' * n if n <= 6 else '888' + '9' * (n - 6) + '888'
        middle = [
            "", "7", "77", "959", "9779", "99799",
            "999999", "9994999", "99944999",
            "999969999", "9999449999", "99999499999"
        ]
        q, r = divmod(n, 12)
        return '999999' * q + middle[r] + '999999' * q
        
# @lc code=end

