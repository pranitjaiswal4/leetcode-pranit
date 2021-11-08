class Solution:

    def majorityElement(self, nums):
        count1 = count2 = 0
        candidate1 = candidate2 = None
        
        for num in nums:                
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        result = list()
        c1, c2 = 0, 0
        
        for num in nums:
            if num == candidate1:
                c1 += 1
            elif num == candidate2:
                c2 += 1
        
        if c1 > len(nums) // 3:
            result.append(candidate1)
        
        if c2 > len(nums) // 3:
            result.append(candidate2)
            
        return result