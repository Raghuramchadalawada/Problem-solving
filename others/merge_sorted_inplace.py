#https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            if nums2[i]>nums1[m-1+i]:
                nums1[m+i]=nums2[i]
            else:
                j=m-1+i
                while j>=0 and nums1[j]>nums2[i]:
                    nums1[j+1]=nums1[j]
                    j-=1
                nums1[j+1]=nums2[i]
        
