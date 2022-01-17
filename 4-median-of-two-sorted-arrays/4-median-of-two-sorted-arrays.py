class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        r = m + n
        
        i, j, k = 0, 0, 0
        
        mid1 = 0
        mid2 = 0
        
        while k <= r//2:
            mid1 = mid2
            if i == m:
                mid2 = nums2[j]
                j += 1
            elif j == n:
                mid2 = nums1[i]
                i += 1
            elif nums1[i] <= nums2[j]:
                mid2 = nums1[i]
                i += 1
            elif nums2[j] < nums1[i]:
                mid2 = nums2[j]
                j += 1
            
            k += 1
        
        if r % 2 == 0:
            return (mid1 + mid2) / 2
        else:
            return mid2
            
        
        