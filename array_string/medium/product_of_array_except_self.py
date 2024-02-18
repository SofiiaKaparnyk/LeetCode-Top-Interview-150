from typing import List

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ls = [1]
        left = right = 1
        for i in range(1, len(nums)):
            left *= nums[i - 1]
            ls.append(left)
        for j in range(2, len(nums) + 1):
            right *= nums[len(nums) - j + 1]
            ls[len(nums) - j] *= right
        return ls


assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
