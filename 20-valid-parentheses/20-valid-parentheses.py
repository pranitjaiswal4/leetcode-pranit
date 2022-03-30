class Solution:
    def isValid(self, s: str) -> bool:
        braces = { ')' : '(', '}' : '{', ']' : '['}
        
        stack = list()
        
        for char in s:
            if char not in braces:
                stack.append(char)
            else:
                elem = stack.pop() if stack else '#'
                
                if elem != braces[char]:
                    return False                        
        
        return not stack
    
    
#     class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = list()
#         braces = { ')': '(', '}' : '{', ']' : '['}
        
#         for i in range(len(s) - 1, -1, -1):
            
#             if s[i] in braces:
#                 stack.append(s[i])
#             else:
#                 if stack:
#                     top = stack[-1]
                
#                     if s[i] == braces[top]:
#                         stack.pop()
#                     else:
#                         return False
#                 else:
#                     return False
                
#         return True if not stack else False
