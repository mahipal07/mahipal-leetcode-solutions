#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# 202/202 cases passed (5 ms)
# Your runtime beats 48.11 % of python3 submissions
# Your memory usage beats 61.41 % of python3 submissions (21.1 MB)

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Map values to their indices in the inorder list for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def recurse(low, high):
            if low > high:
                return None
            
            # The last element in postorder is the root of the current subtree
            root_val = postorder.pop()
            root = TreeNode(root_val)
            
            # Find the split index in the inorder array
            mid = inorder_map[root_val]
            
            # Build the right subtree first because postorder processes Right before Left
            root.right = recurse(mid + 1, high)
            root.left = recurse(low, mid - 1)
            
            return root
        
        return recurse(0, len(inorder) - 1)
        
# @lc code=end

