# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def check(nodeLeft, nodeRight):
            if not nodeLeft and not nodeRight:
                return True
            
            if not nodeLeft or not nodeRight:
                return False
            
            return (nodeLeft.val == nodeRight.val) and check(nodeLeft.left, nodeRight.right) and check(nodeLeft.right, nodeRight.left)
        
        
        return check(root, root)