#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Numbers ending with 0 (but not 0 itself) are not palindromes
        if x % 10 == 0 and x != 0:
            return False

        reversed_half = 0
        while x > reversed_half:
            # Take the last digit and build reversed_half
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even length numbers: x == reversed_half
        # For odd length numbers: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10

        
# @lc code=end

