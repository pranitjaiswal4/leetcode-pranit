class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
      
        minWinLen = m + 1
        output = ""

        freq = dict()
        
        for c in t:
            freq[c] = freq.get(c, 0) + 1
        
        count = len(freq)
        i, j = 0, 0
        
        while j < m:
            
            if s[j] in freq:
                freq[s[j]] -= 1
                
                if freq[s[j]] == 0:
                    count -= 1
            
            while count == 0:
                
                if s[i] in freq:
                    
                    freq[s[i]] += 1
                    
                    if freq[s[i]] == 1:
                        count += 1
                    
                winLen = j - i + 1
                
                if winLen < minWinLen:
                    minWinLen = winLen
                    output = s[i:j+1]
                
                i += 1
            
            j += 1
            
        return output