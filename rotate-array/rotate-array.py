class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums2 = list()
        k = k % len(nums)
        print(len(nums))
        
        for i in range(len(nums) - k, len(nums)):
            nums2.append(nums[i])
        
        for i in range(0, len(nums) - k):
            nums2.append(nums[i])
        
        nums[:] = nums2