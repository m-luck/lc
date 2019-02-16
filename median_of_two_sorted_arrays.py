from math import *
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        combined = []
        for num in nums1:
            combined.append(num)
        for num in nums2:
            combined.append(num)
        combined = sorted(combined)
        median = 0
        len_comb = len(combined)
        if len_comb%2 == 0:
            median = combined[int(len_comb/2)]+combined[int(len_comb/2)-1]
            median = median / 2
        else:
            median = combined[floor(len_comb/float(2))]
        return median
            
