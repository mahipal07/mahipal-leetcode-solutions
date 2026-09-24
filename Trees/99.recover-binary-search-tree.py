#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
# 1919/1919 cases passed (1 ms)
# Your runtime beats 70.74 % of python3 submissions
# Your memory usage beats 40.54 % of python3 submissions (20.3 MB)

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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first = None
        self.second = None
        self.prev = None
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node
            
            inorder(node.right)
            
        inorder(root)
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val
        
# @lc code=end

