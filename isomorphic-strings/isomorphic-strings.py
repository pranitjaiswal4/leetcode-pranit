class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = dict()
        seen = set()
        
        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] not in seen:
                    mapping[s[i]] = t[i]
                    seen.add(t[i])
                else:
                    return False
            else:
                if mapping[s[i]] != t[i]:
                    return False
                
        print(mapping)
                
        return True
        
        