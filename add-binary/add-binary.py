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

        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        i = -1
        sm, carry = "", "0"

        while i >= (n*-1):
            carry, s = addBinaryDigits(a[i], b[i], carry)
            sm = s + sm
            i -= 1

        if carry == "1":
            sm = carry + sm

        return sm
