# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        colDict = dict()
        result = list()
        q = deque()
        minCol = 0
        maxCol = 0

        if not root:
            return

        q.append([root,0])

        while q:
            lq = len(q)
            
            for i in range(lq):
                node, col = q.popleft()

                if col not in colDict:
                    colDict[col] = [node.val]
                else:
                    colDict[col].append(node.val)

                minCol = min(minCol, col)
                maxCol = max(maxCol, col)

                if node.left:
                    q.append([node.left, col-1])
                if node.right:
                    q.append([node.right, col+1])

        for i in range(minCol, maxCol+1):
            result.append(colDict[i])

        return result