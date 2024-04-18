class Solution:
    def validPalindrome(self, s: str) -> bool:
        deleted = 0
        sub1 = sub2 = ""

        def checkPalindrome(str):
            nonlocal deleted
            nonlocal sub1, sub2
            i = 0 
            j = len(str) - 1
            while i <= j:
                if str[i] != str[j]:
                    if deleted == 0:
                        sub1 = str[i+1:j+1]
                        sub2 = str[i:j]
                        deleted = 1
                    return False
                
                i += 1
                j -= 1
            return True

        if checkPalindrome(s):
            return True

        return checkPalindrome(sub1) or checkPalindrome(sub2)