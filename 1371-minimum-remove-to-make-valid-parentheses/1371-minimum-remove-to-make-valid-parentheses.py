class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = list()
        valid = ""
        result = ""

        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append('(')
                valid += '('
            elif s[i] == ')':
                if stack:
                    stack.pop()
                    valid += ')'
            else:
                valid += s[i]

            i += 1

        for i in range(len(valid)-1, -1, -1):
            if stack:
                if valid[i] == '(':
                    stack.pop()
                else:
                    result += valid[i]
            else:
                result += valid[i]        
        
        result = result[::-1]
        return result
