class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result, start, end = 1, 0, 0
        
        while end < len(nums) - 1:
            if nums[end] >= nums[end + 1]:
                start = end + 1
            
            end += 1
            result = max(result, end - start + 1)


        return result
            
        