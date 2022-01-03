class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:       
        output = nums[::]
        
        for i in range(len(output) - 2, -1, -1):
            output[i] *= output[i+1]
            
        left = 1
        
        for i in range(len(output) - 1):
            output[i] = left * output[i+1]
            left *= nums[i]
        
        output[-1] = left
        
        return output