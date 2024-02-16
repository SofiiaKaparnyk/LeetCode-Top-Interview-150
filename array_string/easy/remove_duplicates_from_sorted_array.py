from typing import List, Tuple

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each 
unique element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present 
in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> Tuple[int, List[int]]:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j, nums


assert Solution().removeDuplicates([1, 1, 2]) == (2, [1, 2, 2])
assert Solution().removeDuplicates([1, 2, 3]) == (3, [1, 2, 3])
assert Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == (
    5,
    [0, 1, 2, 3, 4, 2, 2, 3, 3, 4],
)
