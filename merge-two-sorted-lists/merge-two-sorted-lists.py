# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def createLinkedList(resultLinkedList: list()) -> ListNode :
    output = ListNode()
    node = ListNode()

    
    if len(resultLinkedList) == 1:
        node.val = resultLinkedList[0].val
        node.next = None
        # print(node)
        return node
    
    node.val = resultLinkedList[0].val
    node.next = createLinkedList(resultLinkedList[1:])

    # print(node)
    return node

class Solution:
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        # print(l1)
        # print(l2)
        
        if not l1:
            if not l2:
                return l1
            else:
                return l2
        else:
            if not l2:
                return l1
            else:
                
                while l1 is not None and l2 is not None:
                    if l1.val < l2.val:
                        result.append(l1.val)
                        l1 = l1.next
                    elif l1.val > l2.val:
                        result.append(l2.val)
                        l2 = l2.next
                    else:
                        result.append(l1.val)
                        result.append(l2.val)
                        l1 = l1.next
                        l2 = l2.next
                    
                
                while l1 is not None:
                    result.append(l1.val)
                    l1 = l1.next
                    
                    
                while l2 is not None:
                    result.append(l2.val)
                    l2 = l2.next
                
                print(result)
                
                
                resultLinkedList = []
                output = []
                
                i=0
                while i < (len(result)-1):
                    finalResult = ListNode(result[i], ListNode(result[i+1]))
                    resultLinkedList.append(finalResult)
                    i+=1
                
                # print(f'i:{i}')
                
                finalResult = ListNode(result[i], None)
                resultLinkedList.append(finalResult)
                
                print(resultLinkedList)
                print("\n")


                output = createLinkedList(resultLinkedList)
                
                print(output)
                return output 
            