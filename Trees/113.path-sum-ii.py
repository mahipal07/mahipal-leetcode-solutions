#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# 115/115 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 65.1 % of python3 submissions (20.1 MB)

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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node, current_sum, path):
            if not node:
                return
            
            current_sum += node.val
            path.append(node.val)
            
            if not node.left and not node.right:
                if current_sum == targetSum:
                    res.append(list(path))
            else:
                dfs(node.left, current_sum, path)
                dfs(node.right, current_sum, path)
                
            path.pop()
            
        dfs(root, 0, [])
        return res
    
# @lc code=end

