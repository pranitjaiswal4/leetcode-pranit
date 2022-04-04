class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        
        j=len(num)-1
        
        
        for i in range(int(len(num)/2)):
            if num[i] != num[j]:
                return False
            
            j-=1
            
        return True
            
            
            