# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        ans_left = []
        ans_right = []
        
        def inorder(node, level):
            
            if not node:
                return
            
            level += 1
            
            inorder(node.left, level)
            ans_left.append(str(node.val) + str(level))
            inorder(node.right, level)
        
        def rev_inorder(node, level):
            if not node:
                return
            
            level += 1
            
            rev_inorder(node.right, level)
            ans_right.append(str(node.val) + str(level))
            rev_inorder(node.left, level)
        
        
        inorder(root, 0)
        rev_inorder(root, 0)
        
        # print(ans_left)
        # print(ans_right)
        
        if ans_left == ans_right:
            return True
        
        return False
        