class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        longest = 0
        
        if k == 0:
            return 0
        
        n = len(s)
        i, j = 0, 0
        
        freq = dict()
        
        while j < n:
            freq[s[j]] = freq.get(s[j], 0) + 1
            
            if len(freq) > k:
                
                while i < j:
                    
                    if s[i] in freq:
                        freq[s[i]] -= 1

                        if freq[s[i]] == 0:
                            freq.pop(s[i])
                    
                    i += 1
                    
                    if len(freq) == k:
                        break
            
            longest = max(longest, j - i + 1)
            
            j += 1
            
        return longest
