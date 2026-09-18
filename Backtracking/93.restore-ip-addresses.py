#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
# 146/146 cases passed (2 ms)
# Your runtime beats 52.8 % of python3 submissions
# Your memory usage beats 29.47 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str):
        res = []

        def backtrack(start, parts):
            # If 4 parts are formed and all digits are used
            if len(parts) == 4 and start == len(s):
                res.append(".".join(parts))
                return
            
            # Stop if too many parts
            if len(parts) >= 4:
                return

            # Try 1 to 3 digit segments
            for length in range(1, 4):
                if start + length > len(s):
                    break
                segment = s[start:start+length]
                
                # Skip invalid segments
                if (segment.startswith("0") and len(segment) > 1) or int(segment) > 255:
                    continue
                
                backtrack(start+length, parts+[segment])

        backtrack(0, [])
        return res
        
# @lc code=end

