#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr = 0
        p_ptr = 0
        match_ptr = 0
        star_idx = -1
        
        while s_ptr < len(s):
            # 1. Direct match or '?' wildcard
            if p_ptr < len(p) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            
            # 2. Found a '*' wildcard: save the state
            elif p_ptr < len(p) and p[p_ptr] == '*':
                star_idx = p_ptr
                match_ptr = s_ptr
                p_ptr += 1
            
            # 3. No match, but we saw a '*' previously: backtrack
            elif star_idx != -1:
                p_ptr = star_idx + 1
                match_ptr += 1
                s_ptr = match_ptr
            
            # 4. No match and no '*' to save us
            else:
                return False
        
        # Check for remaining characters in pattern (only '*' allowed)
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
            
        return p_ptr == len(p)
    
# @lc code=end

