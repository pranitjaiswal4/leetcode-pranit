"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        anc = set()

        def getAncestors(node):
            anc.add(node.val)

            if node.parent:
                getAncestors(node.parent)

        def getLCA(node):
            if node.val in anc:
                return node
            
            if node.parent:
                return getLCA(node.parent)

        getAncestors(p)
        return getLCA(q)