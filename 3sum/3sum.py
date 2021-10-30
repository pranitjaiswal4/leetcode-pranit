class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if not nums or len(nums) < 3:
            return []
        
        result = set()
        seen = dict()
        dups = set()
        
        for i, n1 in enumerate(nums):
            if n1 not in dups:
                dups.add(n1)
                
            for j, n2 in enumerate(nums[i+1:]):
                complement = - n1 - n2
                
                if complement in seen and seen[complement] == i:
                    result.add(tuple(sorted([n1, n2, complement])))
                    
                seen[n2] = i
        
        return result