class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -inf
        currentSum = -inf
        
        for i in range(len(nums)):
            currentSum += nums[i]
            
            if currentSum <= nums[i]:
                currentSum = nums[i]
            
            if currentSum > maxSum:
                maxSum = currentSum
        
        return maxSum