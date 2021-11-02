class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        
        minWinLen = m + 1
        minWindow = ""
        
        if m < n or m == 0 or n == 0:
            return ""
        
        tdict = dict()
        
        for c in t:
            tdict[c] = tdict.get(c, 0) + 1
            
        # print(tdict)
        count = len(tdict)
        
        i, j = 0, 0
        
        while j < m:
            if s[j] in tdict:
                
                tdict[s[j]] -= 1
                
                if tdict[s[j]] == 0:
                    count -= 1
                    
            # print(s[j], tdict, count, s[i:j+1])
                    
            while count == 0:
                winLen = j - i + 1

                if winLen <= minWinLen:
                    minWinLen = winLen
                    minWindow = s[i:j+1]
                    
                if s[i] in tdict:
                    tdict[s[i]] += 1
                    
                    if tdict[s[i]] == 1:
                        count += 1
                        
                i += 1
                                    
            j += 1
            
        return minWindow
