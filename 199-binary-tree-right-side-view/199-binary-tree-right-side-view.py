# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        visited = set()
        
        def dfs(node, level):
            nonlocal result
            nonlocal visited
            
            if not node:
                return
            
            level += 1
            
            if level not in visited:
                visited.add(level)
                result.append(node.val)
            
            if node.right:
                dfs(node.right, level)
            
            if node.left:
                dfs(node.left, level)
        
        
        dfs(root, 0)
        return result
        