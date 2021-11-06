# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        max_level = 0
        right_view = []
        

        def dfs(node, level):
            nonlocal max_level
            nonlocal right_view

            if not node:
                return

            level += 1
            if level > max_level:
                max_level = level
                right_view.append(node.val)

            if node.right:
                dfs(node.right, level)
                
            if node.left:
                dfs(node.left, level)

        dfs(root, 0)
        return right_view