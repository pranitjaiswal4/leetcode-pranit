class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        
        for i in range(len(strs)):
            word = ''.join(sorted(strs[i]))
            
            if word not in seen:
                seen[word] = [strs[i]]
            else:
                seen[word].append(strs[i])
        
        result = list(seen.values())
        return result