class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        n = len(s)
        i, j = 0, 0
        
        visited = set()

        while j < n:
            if s[j] not in visited:
                visited.add(s[j])
                max_count = max(max_count, j-i+1)
            else:
                max_count = max(max_count, j-i)
                
                while i < j:
                    if s[i] == s[j]:
                        i += 1
                        break
                        
                    visited.remove(s[i])
                    i += 1
                
            j += 1
                        
        return max_count