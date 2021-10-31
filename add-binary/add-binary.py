class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        def addBinaryDigits(x, y, c):
            if x == "1" and y == "1":
                if c == "1":
                    return "1", "1"
                else:
                    return "1", "0"
            elif x == "0" and y == "0":
                if c == "1":
                    return "0", "1"
                else:
                    return "0", "0"
            else:
                if c == "1":
                    return "1", "0"
                else:
                    return "0", "1"
        
        n = 1
        lena = len(a)
        lenb = len(b)
        
        if lena >=lenb:
            n = lena
        else:
            n = lenb
        
        i = -1
        sm, carry = "", "0"
        
        while i >= (n*-1):
            c, s = "0", "0"
            
            if lena >= -i and lenb >= -i:
                c,s = addBinaryDigits(a[i], b[i], carry)
            elif lena >= -i:
                c,s = addBinaryDigits(a[i], "0", carry)
            elif lenb >= -i:
                c,s = addBinaryDigits("0", b[i], carry)
                
            carry = c
            sm = s + sm

            i -= 1
        
        if carry == "1":
            sm = carry + sm
            
        return sm