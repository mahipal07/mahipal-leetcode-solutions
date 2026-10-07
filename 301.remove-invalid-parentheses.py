#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#
# 129/129 cases passed (71 ms)
# Your runtime beats 70.59 % of python3 submissions
# Your memory usage beats 62.94 % of python3 submissions (19.6 MB)

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = {s}
        
        while queue:
            # Filter all valid strings at the current removal level
            valid = list(filter(is_valid, queue))
            if valid:
                return valid
            
            # Generate the next level by removing one parenthesis at each position
            next_queue = set()
            for current in queue:
                for i, char in enumerate(current):
                    if char in "()":
                        next_queue.add(current[:i] + current[i + 1:])
            queue = next_queue

        return [""]
    
# @lc code=end

