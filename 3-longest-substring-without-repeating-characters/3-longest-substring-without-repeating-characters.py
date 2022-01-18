class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        longest = 0
        n = len(s)
        i, j = 0, 0
        visited = set()
        
        while j < n:
            
            if s[j] not in visited:
                visited.add(s[j])
            else:
                while i < j:
                    if s[i] == s[j]:
                        i += 1
                        break
                        
                    visited.remove(s[i])
                    i += 1
                    
            longest = max(longest, j - i + 1)
            
            j += 1
        
        return longest