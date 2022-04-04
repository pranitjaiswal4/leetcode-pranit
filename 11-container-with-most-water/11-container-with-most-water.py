class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        
        n = len(height)
        
        i = 0
        j = n - 1
        
        while i < j:
            area = (j - i) * min(height[i], height[j])
            
            maxArea = max(maxArea, area)            
            
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
                    
        return maxArea