# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        
        def dfs(node, level):
            nonlocal max_depth
            
            if not node:
                return
            
            level += 1
            max_depth = max(max_depth, level)
            
            if not node.left and not node.right:
                return
                
            if node.left:
                dfs(node.left, level)
            if node.right:
                dfs(node.right, level)            
                
        dfs(root, 0)
        
        return max_depth