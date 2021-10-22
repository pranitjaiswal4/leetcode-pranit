class Solution:
    def isHappy(self, n: int) -> bool:
        source = n
        seen = set()
    
        def isReallyHappy(n):
            sourceExist = 0
            allZeros = 1
            
            seen.add(n)
            
            if n == 1:
                return True
            
            nums = list()
            nums = [int(c) for c in str(n)]
            
#             for c in str(n):
#                 if int(c) == source:
#                     sourceExist = 1
#                 elif int(c) != 0:
#                     allZeros = 0
                    
#                 nums.append(int(c))
                
            print(nums)
            
            # if sourceExist == 1 and allZeros == 1 and len(nums) > 1:
            #     return False
            
            sum = 0
            for num in nums:
                sum += num**2

            print(sum)
            
            if sum in seen:
                return False

            return isReallyHappy(sum)
        
        return isReallyHappy(n)