from typing import List

"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        step = k % len(nums)
        nums[:] = nums[-step:] + nums[:-step]
        return nums


assert Solution().rotate([1, 2, 3, 4, 5, 6], 3) == [4, 5, 6, 1, 2, 3]
assert Solution().rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
