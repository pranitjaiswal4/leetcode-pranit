# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        max_depth = 0
        
        def dfs(node, depth):
            nonlocal max_depth
            
            if not node:
                return
            
            depth += 1
            max_depth = max(max_depth, depth) 
            
            if node.left:
                dfs(node.left, depth)
                
            if node.right:
                dfs(node.right, depth)
                    
        dfs(root, 0)
        
        return max_depth