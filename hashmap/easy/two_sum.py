from typing import List

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            d[target - nums[i]] = i


assert Solution().twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
assert Solution().twoSum(nums=[3, 2, 4], target=6) == [1, 2]
assert Solution().twoSum(nums=[3, 3], target=6) == [0, 1]
