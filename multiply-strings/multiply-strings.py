class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1 == "0" or num2 == "0":
            return "0"
        
        ans = [0 for i in range(len(num1) + len(num2))]
        
        n1 = num1[::-1]
        n2 = num2[::-1]
        
        for i in range(len(n1)):
            for j in range(len(n2)):
                carry = ans[i+j]
                x = int (n1[i]) * int(n2[j]) + carry
                
                # last digit
                ans[i+j] = x % 10
                
                # new carry
                ans[i+j+1] += x // 10
                
        if ans[-1] == 0:
            ans.pop()
            
        ans = ans[::-1]
        
        return ''.join(str(i) for i in ans)