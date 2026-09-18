#
# @lc app=leetcode id=1520 lang=python3
#
# [1520] Maximum Number of Non-Overlapping Substrings
#
# 285/285 cases passed (283 ms)
# Your runtime beats 37.17 % of python3 submissions
# Your memory usage beats 9.73 % of python3 submissions (30.2 MB)

# @lc code=start
class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {c: i for i, c in reversed(list(enumerate(s)))}
        last = {c: i for i, c in enumerate(s)}

        intervals = []
        for c in set(s):
            left, right = first[c], last[c]
            valid = True
            i = left
            while i <= right:
                ch = s[i]
                if first[ch] < left:
                    valid = False
                    break
                right = max(right, last[ch])
                i += 1

            if valid:
                intervals.append((right, left))

        intervals.sort()

        ans = []
        prev_end = -1
        for right, left in intervals:
            if left > prev_end:
                ans.append(s[left : right + 1])
                prev_end = right

        return ans
    
# @lc code=end

