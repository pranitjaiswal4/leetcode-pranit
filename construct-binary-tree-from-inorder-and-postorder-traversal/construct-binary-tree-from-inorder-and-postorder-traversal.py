# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        indict = {key:i for i, key in enumerate(inorder)}
        postIndex = len(postorder) - 1
        
        def processTree(startIn, endIn):
            nonlocal postIndex
            
            if startIn > endIn:
                return
            
            root = postorder[postIndex]
            inIndex = indict[root]
            
            postIndex -= 1
            node = TreeNode(root)            
            node.right = processTree(inIndex + 1, endIn)
            node.left = processTree(startIn, inIndex - 1)        
            
            return node
        
        return processTree(0, len(inorder) - 1)
            