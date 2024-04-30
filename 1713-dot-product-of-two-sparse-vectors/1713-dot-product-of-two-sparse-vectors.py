class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = dict()

        for i in range(len(nums)):        
            if nums[i] != 0:
                self.nonzeros[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0

        for i in self.nonzeros:
            if i in vec.nonzeros:
                result += (self.nonzeros[i] * vec.nonzeros[i])
        
        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)