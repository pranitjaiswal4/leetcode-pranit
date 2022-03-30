class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        braces = { ')': '(', '}' : '{', ']' : '['}
        
        for i in range(len(s) - 1, -1, -1):
            
            if s[i] in braces:
                stack.append(s[i])
            else:
                if stack:
                    top = stack[-1]
                
                    if s[i] == braces[top]:
                        stack.pop() if stack else '#'
                    else:
                        return False
                else:
                    return False
                
        return True if not stack else False