class Solution:   
    def rob(self, nums: List[int]) -> int:
        
        def checkRob(val, n):
            if n <= 0:
                t[n] = 0
                return t[n]

            if t[n] != -1:
                return t[n]

            t[n] = max(val[n-1] + checkRob(val, n-2),
                       checkRob(val, n-1))

            return t[n]
        
        
        n = len(nums)
        t = [-1 for i in range(n+1)]
        return checkRob(nums, n)