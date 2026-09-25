#
# @lc app=leetcode id=1096 lang=python3
#
# [1096] Brace Expansion II
#
# 115/115 cases passed (3 ms)
# Your runtime beats 79.78 % of python3 submissions
# Your memory usage beats 29.51 % of python3 submissions (19.6 MB)

# @lc code=start
class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        cur_set = {''}
        union_set = set()

        for ch in expression:
            if ch.isalpha():
                cur_set = {w + ch for w in cur_set}
            elif ch == '{':
                stack.append((union_set, cur_set))
                union_set, cur_set = set(), {''}
            elif ch == ',':
                union_set |= cur_set
                cur_set = {''}
            elif ch == '}':
                union_set |= cur_set
                prev_union, prev_cur = stack.pop()
                cur_set = {w1 + w2 for w1 in prev_cur for w2 in union_set}
                union_set = prev_union

        return sorted(union_set | cur_set)
     
# @lc code=end

