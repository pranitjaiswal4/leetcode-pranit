# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        common = None
        
        def dfs(node):
            nonlocal common
            
            if not node: return 0
            count = 0
            
            if not common:
                count += dfs(node.left)
            if not common:
                count += dfs(node.right)

            if node == p: count += 1
            if node == q: count += 1
            
            if not common and count >= 2:
                common = node
            
            return count
        
        dfs(root)
        
        return common
