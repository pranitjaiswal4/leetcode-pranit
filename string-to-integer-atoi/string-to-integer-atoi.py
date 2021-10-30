class Solution:
    def myAtoi(self, s: str) -> int:
        countSpaces = 0
        
        i = 0
        n = len(s)
        sign = 1
        signSelected = 0
        start = -1
        numStarted = False
        num = 0
        numLength = 0
        
        while i < n:
            if s[i] == ' ' and signSelected == 0:
                countSpaces += 1
            elif s[i] == ' ' and signSelected == 1:
                break
            else:
                if s[i] == '-' :
                    if signSelected == 0:
                        signSelected = 1
                        sign = -1
                        # print("A. sign assigned here:", sign)

                    else: break
                elif s[i] == '+':
                    if signSelected == 0:
                        signSelected = 1
                        sign = +1
                        # print("B. sign assigned here:", sign)
                    else: break
                elif not s[i].isdigit():
                    break
                elif s[i].isdigit():                    
                    if signSelected == 0:
                        signSelected = 1
                        sign = 1
                        # print("C. sign assigned here:", sign)
                        
                    if not numStarted:
                        numStarted = True
                        start = i
                                
                    if numStarted:
                        numLength += 1
                    
                
                # print(s[i])
            i += 1
        
        # print("before s:", s, start, start+numLength)
        
        if numLength > 0:
            s = s[start:start+numLength]

            # print("after s:", s)

            num = int(s)
            # print("before num:", num, sign)
            num = num * sign

            # print("after num:", num, sign)

            if num < -1 * math.pow(2,31):
                num = -1 * math.pow(2,31)
            elif num > math.pow(2,31) - 1:
                num = math.pow(2,31) - 1

        return int(num)
                
            