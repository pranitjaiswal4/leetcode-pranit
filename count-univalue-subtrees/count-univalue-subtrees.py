# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count = 0
        
        def dfs(node):
            nonlocal count
            left_val, right_val = None, None
            
            if not node.left and not node.right:
                count += 1
                return node.val
            
            if node.left:
                left_val = dfs(node.left)
                
            if node.right:
                right_val = dfs(node.right)
            
            if left_val == node.val and right_val == node.val:
                count += 1
                return node.val

            elif left_val == node.val and not right_val:
                count += 1
                return node.val
                
            elif right_val == node.val and not left_val:
                count += 1
                return node.val
            
            return -5000
            
        if not root:
            return 0
        
        dfs(root)
        
        return count