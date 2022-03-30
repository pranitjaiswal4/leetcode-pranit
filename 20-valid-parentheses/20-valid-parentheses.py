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