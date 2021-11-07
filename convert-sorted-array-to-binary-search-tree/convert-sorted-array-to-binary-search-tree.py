# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def processTree(start, end):
            if start > end:
                return None
            
            mid = (start + (end - start) // 2) 
            root = TreeNode(nums[mid])

            root.left = processTree(start, mid - 1)
            root.right = processTree(mid + 1, end)
                    
            return root
            
        return processTree(0, len(nums) - 1)


# ALTERNATE SOLUTION
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
#         def processTree(numlist):
#             root = None
            
#             if len(numlist) > 1:
#                 mid = len(numlist) // 2
#                 root = TreeNode(numlist[mid])
#                 leftList = numlist[:mid]
#                 rightList = numlist[mid+1:]
            
#                 # print(leftList, rightList)

#                 if leftList:
#                     root.left = processTree(leftList)

#                 if rightList:
#                     root.right = processTree(rightList)
                    
#             else:
#                 root = TreeNode(numlist[0])
                
#             return root
            
#         return processTree(nums)

