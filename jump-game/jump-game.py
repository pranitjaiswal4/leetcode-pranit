class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        if nums[0] >= n - 1:
            return True
        
        valid = False
        for i in range(n-1):
            if i + nums[i] >= n - 1:
                valid = True
        
        def checkJump(i, jump_no):
            if i < n:
                if i == n - 1:
                    t[i] = True
                    return t[i]

                if jump_no == nums[i]:
                    t[i] = False
                    return t[i]

                if i + (nums[i] - jump_no) == n - 1:
                    t[i] = True
                    return t[i]

                if t[i] != -1:
                    return t[i]

                t[i] = checkJump(i + (nums[i] - jump_no), 0) or checkJump(i, jump_no+1)
                return t[i]
        
        t = [-1 for i in range(n)]
        
        if valid:
            return checkJump(0, 0)