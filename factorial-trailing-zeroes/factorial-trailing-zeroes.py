class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        maxPow5 = 0
        mult = 1
        
        while mult < n:
            mult *= 5
            maxPow5 += 1
        
        print("maxPow5:", maxPow5)
        
        for i in range(1, maxPow5+1):
            result += n // int(math.pow(5, i))
            # print(result)
        
        return result