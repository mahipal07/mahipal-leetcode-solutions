#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] Smallest Subsequence of Distinct Characters
#
# 68/68 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 95.34 % of python3 submissions (19.2 MB)

# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            if char in seen:
                continue
                
            while stack and char < stack[-1] and last_occurrence[stack[-1]] > i:
                seen.remove(stack.pop())
                
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)
    
# @lc code=end

