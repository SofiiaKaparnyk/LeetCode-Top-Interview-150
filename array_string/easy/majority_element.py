
from typing import List

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
always exists in the array.
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


assert Solution().majorityElement([3,2,3]) == 3
assert Solution().majorityElement([1]) == 1
assert Solution().majorityElement([2,2,1,1,1,2,2]) == 2