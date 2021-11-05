# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        targetAchieved = False
        
        def dfs(node, sum):
            nonlocal targetAchieved
            
            if targetAchieved:
                return
            
            if not node:
                return
            
            sum += node.val
            
            if not node.left and not node.right:
                if sum == targetSum:
                    targetAchieved = True
                    return
                
            if node.left:
                dfs(node.left, sum)
            if node.right:
                dfs(node.right, sum)
                
                
        dfs(root, 0)
        
        return targetAchieved