class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        output = list()
        
        while i < m and j < n:
            if nums2[j] < nums1[i]:
                output.append(nums2[j])
                j+=1
            else:
                output.append(nums1[i])
                i+=1
        
        while i < m:
            output.append(nums1[i])
            i+=1
        
        while j < n:
            output.append(nums2[j])
            j+=1
        
        for k in range(len(output)):
            nums1[k] = output[k]
        
        # return nums1