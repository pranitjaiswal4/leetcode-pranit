class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = dict()
        result = list()
        
        for i in range(len(nums)):
            if nums[i] not in numDict:
                numDict[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numDict and i != numDict[diff]:
                return [i, numDict[diff]]