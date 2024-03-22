from typing import List

"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, len(nums1)):
            nums1.pop()
        nums1.extend(nums2[:n])
        nums1.sort()
        return nums1


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        nums1 = nums1[:m]
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                if i == 0:
                    nums1.insert(0, nums2[j])
                else:
                    nums1.insert(i - 1, nums2[j])
                j += 1
            else:
                i += 1

        if j < n:
            nums1.extend(nums2[j:n])

        return nums1


assert Solution().merge([1, 2, 3], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
assert Solution().merge([1], 1, [], 0) == [1]
assert Solution().merge([0], 0, [1], 1) == [1]
