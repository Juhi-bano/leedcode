class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        n = len(nums3)
        if n % 2 == 1:
            return nums3[n//2]
        else:
            mid1 = nums3[n//2]
            mid2 = nums3[(n//2)-1]
            return (mid1 + mid2)/2
        