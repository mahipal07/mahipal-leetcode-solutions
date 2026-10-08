#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# 53/53 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 85.48 % of python3 submissions (44.4 MB)

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = collections.deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            
            if not node.left and not node.right:
                return depth
                
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
# @lc code=end

