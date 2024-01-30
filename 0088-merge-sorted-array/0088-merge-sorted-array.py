class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1 += nums2        
        
        if len(nums1) > m+n:
            nums1[:] = [i for i in nums1 if i!=0]
            
        if len(nums1) < m+n:
            nums1 += [0] * (m+n-len(nums1))
            
        nums1.sort()