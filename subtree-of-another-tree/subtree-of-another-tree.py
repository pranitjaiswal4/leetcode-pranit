# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(node, sub):
            
            if not node and not sub:
                return True
            
            elif node and sub:
                return node.val == sub.val and isSame(node.left, sub.left) and isSame(node.right, sub.right)
            else:
                return False
            
        return bool(root and subRoot) and (isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        
