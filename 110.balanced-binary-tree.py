#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# 228/228 cases passed (3 ms)
# Your runtime beats 51.37 % of python3 submissions
# Your memory usage beats 18.81 % of python3 submissions (20.6 MB)

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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0
            
            left = check(node.left)
            if left == -1:
                return -1
                
            right = check(node.right)
            if right == -1:
                return -1
                
            if abs(left - right) > 1:
                return -1
                
            return max(left, right) + 1
            
        return check(root) != -1
        
# @lc code=end

