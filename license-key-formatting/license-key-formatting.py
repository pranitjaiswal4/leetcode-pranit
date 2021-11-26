class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        output = ""
        count = 0
        
        for i in range(len(s) - 1, -1, -1):
            
            if s[i].isalnum():
                if count == k:
                    count = 0
                    output += "-"
                
                output += s[i].upper()
                count += 1
                
        return output[::-1]