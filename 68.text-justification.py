#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
# 29/29 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 85.73 % of python3 submissions (19.3 MB)

# @lc code=start
class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur.append(w)
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]
      
# @lc code=end

