# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        
        def dfs(node, level):
            nonlocal ans
            
            if not node:
                return
            
            level += 1
            
            if len(ans) < level:
                ans.append(node.val)
            
            # main logic is here
            
            
            if node.right:
                dfs(node.right, level)
                
            if node.left:
                dfs(node.left, level)
        
        
        dfs(root, 0)
        return ans