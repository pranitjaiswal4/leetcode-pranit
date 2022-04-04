class Solution:
    def romanToInt(self, s: str) -> int:
        
        romanNum = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    
        sum = 0
        length = len(s)
                
        if length == 1:
            return romanNum[s]
        
        i=0
        
        while i < length-1:
            if romanNum[s[i]] < romanNum[s[i+1]]:
                sum = sum + romanNum[s[i+1]] - romanNum[s[i]]
                i+=2
            else:
                sum = sum + romanNum[s[i]]
                i+=1
                
        
        if i < length:
            sum = sum + romanNum[s[length-1]]
            
        
        return sum
                