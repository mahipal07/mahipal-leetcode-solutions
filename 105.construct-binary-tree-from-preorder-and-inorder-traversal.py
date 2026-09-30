#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# 203/203 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 65.51 % of python3 submissions (21 MB)

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map to look up the index of any value in the inorder traversal in O(1) time
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def helper(left_in, right_in):
            nonlocal pre_idx
            
            # If there are no elements to construct the subtree
            if left_in > right_in:
                return None

            # Select the pre_idx element as the root and increment it
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            # Root splits inorder list into left and right subtrees
            pivot = inorder_map[root_val]

            # Build left and right subtrees
            root.left = helper(left_in, pivot - 1)
            root.right = helper(pivot + 1, right_in)
            
            return root

        return helper(0, len(inorder) - 1)
    
# @lc code=end

