"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        maxDepth = 0
        
        def dfs(node, level):
            nonlocal maxDepth
            
            if not node:
                return
            
            level += 1
            
            if not node.children:
                maxDepth = max(maxDepth, level)
                
            for child in node.children:
                dfs(child, level)
        
        dfs(root, 0)
        
        return maxDepth