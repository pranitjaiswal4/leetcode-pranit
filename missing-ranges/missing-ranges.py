class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        output = list()
        
        val = lower
        count = 0
        
        if not nums:
            if upper == lower:
                return [str(lower)]
            else:
                return [f'{lower}->{upper}']
        
        for i in range(len(nums)):
            if val != nums[i]:
                
                if nums[i] - val == 1:
                    output.append(str(val))
                else:
                    s = f'{val}->{(nums[i] - 1)}'
                    output.append(s)

            val = nums[i] + 1
            
        if upper != nums[-1]:
            if upper - nums[-1] == 1:
                output.append(str(upper))
            else:
                s = f'{val}->{upper}'
                output.append(s)
            
        
        return output