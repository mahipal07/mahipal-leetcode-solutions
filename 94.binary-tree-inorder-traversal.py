#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

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
# 71/71 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 28.58 % of python3 submissions (19.4 MB)

class Solution:
    def inorderTraversal(self, root: TreeNode):
        result, stack = [], []
        current = root

        while current or stack:
            while current:          # Go left as far as possible
                stack.append(current)
                current = current.left
            current = stack.pop()   # Visit node
            result.append(current.val)
            current = current.right # Move to right subtree

        return result


# @lc code=end

