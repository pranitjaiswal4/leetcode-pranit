class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev = s[::-1]
        print(rev)
        m = len(s)
        n = len(rev)
        
        t = [[-1 for i in range(n+1)] for j in range(m+1)]
        
        def lcs(m, n):
            if m == 0 or n == 0:
                return 0
            
            if t[m][n] != -1:
                return t[m][n]
            
            if s[m-1] == rev[n-1]:
                t[m][n] = 1 + lcs(m-1, n-1)
                return t[m][n]
            
            t[m][n] = max(lcs(m, n-1), lcs(m-1, n))
            return t[m][n]
        
        
        return lcs(m, n)