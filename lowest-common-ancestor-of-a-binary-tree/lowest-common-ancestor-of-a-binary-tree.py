# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        found = False
        lca = None

        def dfs(node):
            count = 0
            nonlocal found
            nonlocal lca

            if not node:
                return 0

            if node.val == p.val or node.val == q.val:
                count += 1
                
            if not found and node.left:
                count += dfs(node.left)

            if not found and node.right:
                count += dfs(node.right)

            if not found and count == 2:
                found = True
                lca = node

            return count

        dfs(root)
        return lca
