class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)
        
        t = [[-1 for i in range(n+1)] for j in range(m+1)]
        
        def lcs(m, n):
            if m == 0 or n == 0:
                return 0
            
            if t[m][n] != -1:
                return t[m][n]
            
            if text1[m-1] == text2[n-1]:
                t[m][n] = 1 + lcs(m-1, n-1)
                return t[m][n]
            
            t[m][n] = max(lcs(m-1, n), lcs(m, n-1))
            return t[m][n]
                
        
        return lcs(m, n)