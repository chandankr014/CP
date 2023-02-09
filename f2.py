
class Solution(object):
    nums1 = [1,2]
    nums2 = [3,4]
    def findMedianSortedArrays(self, nums1, nums2):
        a3 = nums1+nums2
        a3 = sorted(a3)
        l = len(a3)
        
        # l is odd
        if l%2 != 0:
            mid = l//2
            res = a3[mid]
        else: 
            mid = l/2
            m1 = int(mid+0.5)
            m2 = int(mid-0.5)
            res = (a3[m1] + a3[m2]) / 2

        return res

    x = findMedianSortedArrays(object, nums1=nums1, nums2=nums2)
    print(x)
