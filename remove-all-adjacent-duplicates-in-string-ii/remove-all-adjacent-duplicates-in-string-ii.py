class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = list()
        output = []
        
        for i in range(len(s)):
            if stack and stack[-1][0] == s[i]:
                freq = stack[-1][1]
                if freq == k - 1:
                    stack.pop()
                else:
                    stack[-1] = [s[i], freq + 1]
            else:
                stack.append([s[i], 1])
                
        return ''.join(c[0]*c[1] for c in stack)