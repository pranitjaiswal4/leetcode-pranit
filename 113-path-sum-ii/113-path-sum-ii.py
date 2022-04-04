# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = list()
        path = list()
        
        def dfs(node, total):
            nonlocal path
            
            if not node:
                return
            
            total += node.val
            path.append(node.val)
            
            if not node.left and not node.right:
                if total == targetSum:
                    result.append(path[::])
                    
            if node.left:
                dfs(node.left, total)
                
            if node.right:
                dfs(node.right, total)
            
            path.pop()
        
        dfs(root, 0)
        
        return result
        