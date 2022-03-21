class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxTotal = -inf
        total = 0
        w = 1
        i = j = 0
        
        while j < len(nums):            
            
            total += nums[j]
                
            if w >= k:
                maxTotal = max(maxTotal, total)
                total -= nums[i]
                i += 1
            
            w += 1
            j += 1
        
        return maxTotal/k