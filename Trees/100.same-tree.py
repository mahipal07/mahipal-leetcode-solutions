#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# 67/67 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 33.63 % of python3 submissions (19.3 MB)

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Initialize a queue with the root pairs
        queue = deque([(p, q)])
        
        while queue:
            node_p, node_q = queue.popleft()
            
            # If both are null, continue checking other nodes
            if not node_p and not node_q:
                continue
            # If one is null or values don't match, they aren't identical
            if not node_p or not node_q or node_p.val != node_q.val:
                return False
                
            # Queue the children in the same order
            queue.append((node_p.left, node_q.left))
            queue.append((node_p.right, node_q.right))
            
        return True
    
# @lc code=end

